import pytest

from ai_assistant.core.models import Request, Response
from ai_assistant.core.workflows import BaseWorkflow


class DummyWorkflow(BaseWorkflow):
    def run(self, request: Request) -> Response:
        return Response(output="dummy")


def test_workflow_returns_response():
    workflow = DummyWorkflow()

    response = workflow.run(Request(input="Hello"))

    assert response.output == "dummy"
    
    
def test_base_workflow_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseWorkflow()