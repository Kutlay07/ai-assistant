"""
Integration tests for real LLM providers.

These tests require valid API credentials and internet access.
"""

from ai_assistant.core.llms import OpenAIProvider


def test_generate_returns_string():

    llm = OpenAIProvider()

    response = llm.generate("Say hello in one word.")

    assert isinstance(response, str)
    assert len(response) > 0