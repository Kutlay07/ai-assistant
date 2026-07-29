from ai_assistant.core.tools import MockTool, ToolRegistry


def test_register_adds_tool():

    registry = ToolRegistry()
    tool = MockTool()

    registry.register(tool)

    assert registry.get("mock") is tool


def test_list_returns_registered_tools():

    registry = ToolRegistry()

    registry.register(MockTool())

    assert registry.list() == ["mock"]


def test_get_returns_registered_tool():

    registry = ToolRegistry()
    tool = MockTool()

    registry.register(tool)

    result = registry.get("mock")

    assert result is tool


def test_execute_registered_tool():

    registry = ToolRegistry()

    registry.register(MockTool())

    tool = registry.get("mock")

    result = tool.execute("hello")

    assert result == "Mock tool response: hello"