from ..config.settings import load_settings

from .base_llm import BaseLLM
from .groq_provider import GroqProvider
from .local_provider import LocalProvider
from .mock_llm import MockLLM


def create_llm() -> BaseLLM:
    settings = load_settings()

    provider = settings.llm_provider

    if provider == "groq":
        return GroqProvider()

    if provider == "local":
        return LocalProvider()

    if provider == "mock":
        return MockLLM()

    raise ValueError(f"Unsupported LLM provider: {provider}")