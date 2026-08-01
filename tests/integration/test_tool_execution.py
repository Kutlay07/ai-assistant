from ai_assistant.api.dependencies import get_assistant
from ai_assistant.core.models import ToolCall


def test_assistant_executes_registered_tool():
    assistant = get_assistant()

    result = assistant.execute_tool(
        ToolCall(
            tool_name="mock",
            arguments={"query": "hello"},
        )
    )

    assert result == "Mock tool response: hello"