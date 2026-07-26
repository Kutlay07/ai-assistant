from ..models import Request, Response
from .base_workflow import BaseWorkflow
from ..llms import BaseLLM
from ..prompts import PromptBuilder


class ChatWorkflow(BaseWorkflow):
    """Workflow for handling chat-based interactions"""
    
    def __init__(self, llm: BaseLLM, prompt_builder: PromptBuilder):
        self._llm = llm
        self._prompt_builder = prompt_builder
        
    def run(self, request: Request) -> Response:
        prompt = self._prompt_builder.build(request)
        output = self._llm.generate(prompt)
        
        return Response(output=output)