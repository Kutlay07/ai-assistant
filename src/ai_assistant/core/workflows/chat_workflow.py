from ai_assistant.core.models import Request, Response
from .base_workflow import BaseWorkflow


class ChatWorkflow(BaseWorkflow):
    """Workflow for handling chat-based interactions"""
    
    def run(self, request: Request) -> Response:
        return Response(
            output=f"Chat response: {request.input}"
            )