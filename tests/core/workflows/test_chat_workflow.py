from ai_assistant.core.models import Request, Response
from ai_assistant.core.workflows import ChatWorkflow
from ai_assistant.core.llms import MockLLM
from ai_assistant.core.prompts import PromptBuilder
from ai_assistant.core.memory import MockMemory


def test_chat_workflow_returns_response():
    workflow = ChatWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
    )

    response = workflow.run(Request(input="Hello"))

    assert isinstance(response, Response)


def test_chat_workflow_uses_llm():
    workflow = ChatWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
    )

    response = workflow.run(Request(input="Hello"))

    assert response.output.startswith("Mock response:")
    assert "Hello" in response.output


def test_chat_workflow_preserves_request_input():
    workflow = ChatWorkflow(
        llm=MockLLM(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
    )

    response = workflow.run(Request(input="How are you?"))

    assert response.output.startswith("Mock response:")
    assert "How are you?" in response.output