from ai_assistant.core.models import Request
from ai_assistant.core.workflows import ChatWorkflow


def test_chat_workflow_returns_response():
    workflow = ChatWorkflow()
    
    response = workflow.run(
        Request(input="Hello")
    )
    
    assert response.output == "Chat response: Hello"