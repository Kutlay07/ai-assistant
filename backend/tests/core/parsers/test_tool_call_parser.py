import pytest

from ai_assistant.core.parsers import ToolCallParser


def test_parse_valid_tool_call():
    parser = ToolCallParser()

    tool_call = parser.parse("mock:hello")

    assert tool_call.tool_name == "mock"
    assert tool_call.arguments == {
        "query": "hello",
    }


def test_parse_invalid_tool_call():
    parser = ToolCallParser()

    with pytest.raises(ValueError):
        parser.parse("hello")


from ai_assistant.core.parsers import ToolCallParser


def test_parse_strips_whitespace():
    parser = ToolCallParser()

    tool_call = parser.parse(
        "  mock  :   hello world   "
    )

    assert tool_call.tool_name == "mock"
    assert tool_call.arguments == {
        "query": "hello world",
    }