import pytest

from ai_assistant.core.models import ToolCall
from ai_assistant.core.tools import ToolCallValidator


def test_valid_tool_call_passes():

    validator = ToolCallValidator()

    tool_call = ToolCall(
        tool_name="mock",
        arguments={
            "query": "Hello"
        },
    )

    validator.validate(tool_call)


def test_tool_call_requires_name():

    validator = ToolCallValidator()

    tool_call = ToolCall(
        tool_name="",
        arguments={
            "query": "Hello"
        },
    )

    with pytest.raises(ValueError):
        validator.validate(tool_call)


def test_tool_call_requires_arguments():

    validator = ToolCallValidator()

    tool_call = ToolCall(
        tool_name="mock",
        arguments={},
    )

    with pytest.raises(ValueError):
        validator.validate(tool_call)