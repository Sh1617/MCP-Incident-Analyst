from langchain_ollama import ChatOllama

from backend.app.core.config import settings


def get_ollama_llm():
    return ChatOllama(
        model=settings.OLLAMA_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
        temperature=0,
    )