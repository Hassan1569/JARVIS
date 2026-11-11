from abc import ABC, abstractmethod
import requests
from openai import OpenAI
from app.config import Config
import logging

logger = logging.getLogger(__name__)

class LLMResponse:
    def __init__(self, content: str, raw_response=None):
        self.content = content
        self.raw_response = raw_response

class LLMProvider(ABC):
    @abstractmethod
    def chat(self, messages: list[dict]) -> LLMResponse:
        pass

class OllamaProvider(LLMProvider):
    def __init__(self):
        self.url = f"{Config.OLLAMA_BASE_URL}/api/chat"
        self.model = Config.OLLAMA_MODEL

    def chat(self, messages: list[dict]) -> LLMResponse:
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }
        try:
            response = requests.post(self.url, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return LLMResponse(content=data.get("message", {}).get("content", ""))
        except Exception as e:
            logger.error(f"Ollama API Error: {e}")
            return LLMResponse(content=f"Error: Could not reach Ollama. Ensure it is running. ({str(e)})")

class OpenAICompatProvider(LLMProvider):
    def __init__(self):
        # Use DeepSeek settings if provider is deepseek
        if Config.LLM_PROVIDER == "deepseek":
            api_key = Config.DEEPSEEK_API_KEY
            base_url = Config.DEEPSEEK_BASE_URL
            self.model = Config.DEEPSEEK_MODEL
        else:
            api_key = Config.OPENAI_API_KEY
            base_url = Config.OPENAI_BASE_URL
            self.model = Config.OPENAI_MODEL

        if not api_key:
            logger.warning("No API Key found for OpenAI/DeepSeek.")

        self.client = OpenAI(api_key=api_key or "dummy-key", base_url=base_url)

    def chat(self, messages: list[dict]) -> LLMResponse:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return LLMResponse(content=response.choices[0].message.content)
        except Exception as e:
            logger.error(f"API Error: {e}")
            return LLMResponse(content=f"Error: Could not get response from LLM. ({str(e)})")

def get_llm_provider() -> LLMProvider:
    """Factory method to return the configured LLM provider."""
    if Config.LLM_PROVIDER == "ollama":
        return OllamaProvider()
    elif Config.LLM_PROVIDER in ["openai", "deepseek", "custom"]:
        return OpenAICompatProvider()
    else:
        raise ValueError(f"Unknown LLM_PROVIDER: {Config.LLM_PROVIDER}")