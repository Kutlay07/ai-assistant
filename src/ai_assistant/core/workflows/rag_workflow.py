from ..models import Request, Response
from .base_workflow import BaseWorkflow
from ..llms import BaseLLM
from ..prompts import PromptBuilder
from ..memory import BaseMemory
from ..retrievers import BaseRetriever


class RAGWorkflow(BaseWorkflow):
    """Workflow for retrieval-augmented interactions"""
    
    def __init__(
        self,
        llm: BaseLLM,
        prompt_builder: PromptBuilder,
        retriever: BaseRetriever,
        memory: BaseMemory):
        
        super().__init__()
        
        self._llm = llm
        self._prompt_builder = prompt_builder
        self._retriever = retriever
        self._memory = memory
        
    def run(self, request: Request) -> Response:
        history = self._memory.get_history()
        
        context = self._retriever.retrieve(request.input)
        
        prompt = self._prompt_builder.build(
            request=request,
            history=history,
            context=context,
            template="rag",
        )
        
        output = self._llm.generate(prompt)
        
        self._memory.add_message(request.input)
        self._memory.add_message(output)
        
        return Response(output=output)