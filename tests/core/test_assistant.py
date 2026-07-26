from ai_assistant.core.assistant import Assistant
from ai_assistant.core.models import Request, Response
from ai_assistant.core.workflows import BaseWorkflow


class DummyWorkflow(BaseWorkflow):
    def run(self, request: Request) -> Response:
        return Response(output="dummy")
    
    
def test_assistant_delegates_request_to_workflow():
    workflow = DummyWorkflow()
    assistant = Assistant(workflow)
    
    response = assistant.handle(Request(input="Hello"))
    
    assert response.output == "dummy"