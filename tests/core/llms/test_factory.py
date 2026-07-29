import pytest

from ai_assistant.core.llms import (
    MockLLM,
    OpenAIProvider,
    create_llm,
)


def test_create_mock_llm(monkeypatch):

    monkeypatch.setenv("LLM_PROVIDER", "mock")

    llm = create_llm()

    assert isinstance(llm, MockLLM)


def test_create_openai_provider(monkeypatch):

    monkeypatch.setenv("LLM_PROVIDER", "groq")
    monkeypatch.setenv("LLM_API_KEY", "dummy-key")
    monkeypatch.setenv("LLM_MODEL", "dummy-model")
    monkeypatch.setenv("LLM_BASE_URL", "https://example.com")

    llm = create_llm()

    assert isinstance(llm, OpenAIProvider)


def test_unknown_provider_raises_error(monkeypatch):

    monkeypatch.setenv("LLM_PROVIDER", "unknown")

    with pytest.raises(ValueError):
        create_llm()