import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Root directory setup
ROOT_DIR = Path(__file__).parent.parent
load_dotenv(ROOT_DIR / ".env")

class Config:
    # LLM Settings
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()
    
    # Ollama
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
    
    # OpenAI Compatible (OpenAI, DeepSeek, etc.)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    # DeepSeek specific overrides
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
    DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    # App Settings
    LOG_LEVEL = os.getenv("JARVIS_LOG_LEVEL", "INFO").upper()
    USER_NAME = os.getenv("JARVIS_USER_NAME", "User")

def setup_logging():
    """Sets up basic logging to console and file."""
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Create logs dir if not exists
    logs_dir = ROOT_DIR / "logs"
    logs_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=getattr(logging, Config.LOG_LEVEL, logging.INFO),
        format=log_format,
        handlers=[
            logging.FileHandler(logs_dir / "jarvis.log"),
            logging.StreamHandler()
        ]
    )