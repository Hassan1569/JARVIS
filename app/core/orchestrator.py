from app.core.llm import get_llm_provider, LLMProvider
import logging

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        self.llm: LLMProvider = get_llm_provider()
        self.history = [
            {"role": "system", "content": "You are JARVIS, a helpful AI desktop assistant. Answer concisely."}
        ]

    def process_message(self, user_input: str) -> str:
        """Takes user input, sends to LLM with history, returns response."""
        logger.info(f"User: {user_input}")
        self.history.append({"role": "user", "content": user_input})
        
        # Call LLM
        response = self.llm.chat(self.history)
        
        # Save response to history
        self.history.append({"role": "assistant", "content": response.content})
        logger.info(f"JARVIS: {response.content}")
        
        return response.content