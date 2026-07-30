from ..models import Request, Response
from .base_workflow import BaseWorkflow
from ..llms import BaseLLM
from ..prompts import PromptBuilder
from ..memory import BaseMemory
from collections.abc import Iterator


class ChatWorkflow(BaseWorkflow):
    """Workflow for handling chat-based interactions"""
    
    def __init__(self, llm: BaseLLM, prompt_builder: PromptBuilder, memory: BaseMemory):
        self._llm = llm
        self._prompt_builder = prompt_builder
        self._memory = memory
        
        
    def _build_prompt(self, request: Request) -> str:
        history = self._memory.get_history()
        
        return self._prompt_builder.build(
            request=request,
            history=history,
        )
        
        
    def _save_conversation(
        self, 
        request: Request, 
        response: str,) -> None:
        
        self._memory.add_message(request.input)
        self._memory.add_message(response)
        
        
    def stream(
        self, 
        request: Request, 
        ) -> Iterator[str]:
        
        prompt = self._build_prompt(request)
        
        chunks = []
        
        for chunk in self._llm.stream(prompt):
            chunks.append(chunk)
            yield chunk
            
        response = "".join(chunks)
        
        self._save_conversation(request, response)
        
        
    def run(self, request: Request) -> Response:
        prompt = self._build_prompt(request)
        
        output = self._llm.generate(prompt)
        
        self._save_conversation(request, output)
        
        return Response(output=output)