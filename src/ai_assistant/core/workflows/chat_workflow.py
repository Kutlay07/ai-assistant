from ..models import Request, Response
from .base_workflow import BaseWorkflow
from ..llms import BaseLLM
from ..prompts import PromptBuilder
from ..memory import BaseMemory


class ChatWorkflow(BaseWorkflow):
    """Workflow for handling chat-based interactions"""
    
    def __init__(self, llm: BaseLLM, prompt_builder: PromptBuilder, memory: BaseMemory):
        self._llm = llm
        self._prompt_builder = prompt_builder
        self._memory = memory
        
    def run(self, request: Request) -> Response:
        history = self._memory.get_history()
        
        prompt = self._prompt_builder.build(
            request=request,
            history=history,
        )
        
        output = self._llm.generate(prompt)
        
        self._memory.add_message(request.input)
        self._memory.add_message(output)
        
        return Response(output=output)