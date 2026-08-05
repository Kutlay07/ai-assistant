from ..config import settings

from .base_llm import BaseLLM
from .mock_llm import MockLLM
from .groq_provider import GroqProvider
from .local_provider import LocalProvider


def create_llm() -> BaseLLM:

    provider = settings.get_llm_provider()

    if provider == "groq":
        return GroqProvider()

    if provider == "local":
        return LocalProvider()

    if provider == "mock":
        return MockLLM()

    raise ValueError(f"Unsupported LLM provider: {provider}")