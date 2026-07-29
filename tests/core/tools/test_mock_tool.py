from ai_assistant.core.tools import MockTool


def test_mock_tool_returns_response():
    tool = MockTool()

    result = tool.execute({"query": "Hello"})

    assert result == "Mock tool response: Hello"


def test_mock_tool_returns_string():
    tool = MockTool()

    result = tool.execute({"query": "Hello"})

    assert isinstance(result, str)


from ai_assistant.core.tools import MockTool


def test_name_returns_mock():

    tool = MockTool()

    assert tool.name == "mock"