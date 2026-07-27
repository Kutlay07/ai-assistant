from ai_assistant.core.models import Request, Response
from ai_assistant.core.workflows import AgentWorkflow
from ai_assistant.core.llms import MockLLM
from ai_assistant.core.prompts import PromptBuilder
from ai_assistant.core.memory import MockMemory
from ai_assistant.core.tools import MockTool


def test_agent_workflow_returns_response():
    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
        tool=MockTool(),
    )

    response = workflow.run(Request(input="Hello"))

    assert isinstance(response, Response)


def test_agent_workflow_uses_tool():
    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
        tool=MockTool(),
    )

    response = workflow.run(Request(input="Hello"))

    assert response.output.startswith("Mock tool response:")


def test_agent_workflow_stores_messages():
    memory = MockMemory()

    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=memory,
        tool=MockTool(),
    )

    workflow.run(Request(input="Hello"))

    history = memory.get_history()

    assert "Hello" in history
    assert any(
        message.startswith("Mock tool response:")
        for message in history
    )