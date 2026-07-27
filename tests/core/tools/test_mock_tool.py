from ai_assistant.core.tools import MockTool


def test_mock_tool_returns_response():
    tool = MockTool()

    result = tool.execute("Hello")

    assert result == "Mock tool response: Hello"


def test_mock_tool_returns_string():
    tool = MockTool()

    result = tool.execute("Hello")

    assert isinstance(result, str)