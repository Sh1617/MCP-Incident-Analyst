from backend.app.llm.ollama import get_ollama_llm

class LLMFactory:

    @staticmethod
    def get_llm():
        return get_ollama_llm()