"""
Integration tests for real LLM providers.

These tests require valid API credentials and internet access.
"""
import pytest

from ai_assistant.core.config import settings
from ai_assistant.core.llms import GroqProvider

pytestmark = pytest.mark.skipif(
    not settings.llm_api_key,
    reason="LLM_API_KEY is not configured.",
)

def test_generate_returns_string():

    llm = GroqProvider()

    response = llm.generate("Say hello in one word.")

    assert isinstance(response, str)
    assert len(response) > 0