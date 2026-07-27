from ai_assistant.core.models import Request
from ai_assistant.core.prompts import PromptBuilder


def test_prompt_builder_returns_string():
    builder = PromptBuilder()

    prompt = builder.build(
        request=Request(input="Hello"),
        history=[],
    )

    assert isinstance(prompt, str)


def test_prompt_builder_includes_user_input():
    builder = PromptBuilder()

    prompt = builder.build(
        request=Request(input="Hello"),
        history=[],
    )

    assert "Hello" in prompt


def test_prompt_builder_includes_history():
    builder = PromptBuilder()

    prompt = builder.build(
        request=Request(input="Hello"),
        history=[
            "Hi",
            "How are you?",
        ],
    )

    assert "Hi" in prompt
    assert "How are you?" in prompt