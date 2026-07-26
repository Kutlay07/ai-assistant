from abc import ABC, abstractmethod

from ai_assistant.core.models import Request, Response


class BaseWorkflow(ABC):
    """Defines the execution contract for all workflows"""
    
    @abstractmethod
    def run(self, request: Request) -> Response:
        """Execute the workflow"""
        pass