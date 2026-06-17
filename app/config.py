# config.py
import os
from pathlib import Path
from dotenv import load_dotenv


def load_config() -> dict:
    load_dotenv(Path(__file__).parent.parent / ".env")
    return {
        "ai_provider": os.getenv("AI_PROVIDER", "gemini"),
        "openai_api_key": os.getenv("OPENAI_API_KEY", ""),
        "openai_model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "gemini_api_key": os.getenv("GEMINI_API_KEY", ""),
        "gemini_model": os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
        "ollama_url": os.getenv("OLLAMA_URL", "http://localhost:11434"),
        "ollama_model": os.getenv("OLLAMA_MODEL", "llava"),
        "language": os.getenv("LANGUAGE", "pt-BR"),
    }
