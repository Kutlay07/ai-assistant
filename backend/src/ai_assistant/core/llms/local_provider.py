from .base_llm import BaseLLM


class LocalProvider(BaseLLM):
    """Placeholder for future local LLM integrations (e.g. Ollama, LM Studio)."""

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Local provider is not implemented yet.")