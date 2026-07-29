from ..models import Request, Response, ToolSelection
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
        
        
    def select_tool(self, llm_output: str) -> ToolSelection:
        return ToolSelection(
            tool_name="mock",
            query=llm_output,
        )

        
    def run(self, request: Request) -> Response:
        history = self._memory.get_history()
        
        prompt = self._prompt_builder.build(
            request=request,
            history=history,
        )
        
        llm_output = self._llm.generate(prompt)
        
        selection = self.select_tool(llm_output)

        tool = self._tool_registry.get(selection.tool_name)

        tool_output = tool.execute(selection.query)
        
        self._memory.add_message(request.input)
        self._memory.add_message(tool_output)
        
        return Response(output=tool_output)