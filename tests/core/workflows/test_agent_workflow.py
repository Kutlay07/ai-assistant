import pytest

from ai_assistant.core.models import Request, Response
from ai_assistant.core.workflows import AgentWorkflow
from ai_assistant.core.llms import MockLLM
from ai_assistant.core.prompts import PromptBuilder
from ai_assistant.core.memory import MockMemory
from ai_assistant.core.tools import (
    MockTool,
    ToolRegistry,
    ToolCallValidator)



def test_agent_workflow_returns_response():
    registry = ToolRegistry()
    registry.register(MockTool())

    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
        tool_registry=registry,
        tool_call_validator=ToolCallValidator(),
    )

    response = workflow.run(Request(input="Hello"))

    assert isinstance(response, Response)


def test_agent_workflow_uses_tool():
    registry = ToolRegistry()
    registry.register(MockTool())

    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
        tool_registry=registry,
        tool_call_validator=ToolCallValidator(),
    )

    response = workflow.run(Request(input="Hello"))

    assert response.output.startswith("Mock tool response:")


def test_agent_workflow_stores_messages():
    memory = MockMemory()

    registry = ToolRegistry()
    registry.register(MockTool())

    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=memory,
        tool_registry=registry,
        tool_call_validator=ToolCallValidator(),
    )

    workflow.run(Request(input="Hello"))

    history = memory.get_history()

    assert "Hello" in history
    assert any(
        message.startswith("Mock tool response:")
        for message in history
    )


def test_agent_workflow_creates_tool_call():
    memory = MockMemory()

    registry = ToolRegistry()
    registry.register(MockTool())

    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=memory,
        tool_registry=registry,
        tool_call_validator=ToolCallValidator(),
    )

    selection = workflow._create_tool_call(
        "Hello"
    )

    assert selection.tool_name == "mock"
    assert selection.arguments["query"] == "Hello"


def test_agent_workflow_respects_iteration_limit():
    memory = MockMemory()

    registry = ToolRegistry()
    registry.register(MockTool())

    workflow = AgentWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=memory,
        tool_registry=registry,
        tool_call_validator=ToolCallValidator(),
        max_iterations=2,
    )

    workflow.run(Request(input="Hello"))

    history = memory.get_history()

    tool_messages = [
        message
        for message in history
        if message.startswith("Mock tool response:")
    ]

    assert len(tool_messages) == 2

def test_agent_workflow_requires_positive_iterations():
    registry = ToolRegistry()
    registry.register(MockTool())

    with pytest.raises(ValueError):
        AgentWorkflow(
            llm=MockLLM(),
            prompt_builder=PromptBuilder(),
            memory=MockMemory(),
            tool_registry=registry,
            tool_call_validator=ToolCallValidator(),
            max_iterations=0,
        )
