from ..models import Request, Response
from .base_workflow import BaseWorkflow
from ..llms import BaseLLM
from ..memory import BaseMemory
from ..prompts import PromptBuilder
from ..tools import ToolRegistry


class AgentWorkflow(BaseWorkflow):
    """Workflow for agent-based interactions"""
    
    def __init__(self,
                llm: BaseLLM, 
                prompt_builder: PromptBuilder, 
                memory: BaseMemory, 
                tool_registry: ToolRegistry, 
                ):
        super().__init__()
        
        self._llm = llm
        self._prompt_builder = prompt_builder
        self._memory = memory
        self._tool_registry = tool_registry
        

        
    def run(self, request: Request) -> Response:
        history = self._memory.get_history()
        
        prompt = self._prompt_builder.build(
            request=request,
            history=history,
        )
        
        llm_output = self._llm.generate(prompt)
        
        # TODO: Select tool dynamically based on the LLM output.
        tool = self._tool_registry.get("mock")
        
        tool_output = tool.execute(llm_output)
        
        self._memory.add_message(request.input)
        self._memory.add_message(tool_output)
        
        return Response(output=tool_output)