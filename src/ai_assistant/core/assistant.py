from ai_assistant.core.models import Request, Response
from ai_assistant.core.workflows import BaseWorkflow


class Assistant:
    """Coordinates request execution through a workflow"""
    
    def __init__(self, workflow: BaseWorkflow):
        self._workflow = workflow
        
    def handle(self, request: Request) -> Response:
        return self._workflow.run(request)
    
    def stream(self, request: Request):
        return self._workflow.stream(request)