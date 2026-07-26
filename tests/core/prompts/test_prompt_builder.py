from ai_assistant.core.prompts import PromptBuilder
from ai_assistant.core.models import Request


def test_prompt_builder_returns_request_input():
    builder = PromptBuilder()

    prompt = builder.build(Request(input="Hello"))

    assert prompt == "Hello"


def test_prompt_builder_returns_string():
    builder = PromptBuilder()

    prompt = builder.build(Request(input="Hello"))

    assert isinstance(prompt, str)