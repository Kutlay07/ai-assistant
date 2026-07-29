from ..models import Request, Response, ToolCall
from .base_workflow import BaseWorkflow
from ..llms import BaseLLM
from ..memory import BaseMemory
from ..prompts import PromptBuilder
from ..tools import ToolRegistry, ToolCallValidator
from ..planners import BasePlanner


class AgentWorkflow(BaseWorkflow):
    """Workflow for agent-based interactions"""
    
    def __init__(
        self,
        llm: BaseLLM, 
        prompt_builder: PromptBuilder, 
        memory: BaseMemory,
        planner: BasePlanner,
        tool_registry: ToolRegistry,
        tool_call_validator: ToolCallValidator,
        max_iterations: int = 3,
        ):
        super().__init__()
        
        self._llm = llm
        self._prompt_builder = prompt_builder
        self._memory = memory
        self._planner = planner
        self._tool_registry = tool_registry
        self._tool_call_validator = tool_call_validator
        self._max_iterations = max_iterations
        
        if max_iterations < 1:
            raise ValueError(
                "max_iterations must be greater than 0."
            )
        
        
    def _create_tool_call(self, llm_output: str) -> ToolCall:
        return ToolCall(
            tool_name="mock",
            arguments={
                "query": llm_output,
            },
        )

        
    def run(self, request: Request) -> Response:
        self._memory.add_message(request.input)
        
        history = self._memory.get_history()
        
        plan = self._planner.create_plan(request)
        
        tool_output = ""
        
        for step in plan.steps:
            
            prompt = self._prompt_builder.build(
                request=request,
                history=history,
                current_step=step,
            )
            
            llm_output = self._llm.generate(prompt)
            
            tool_call = self._create_tool_call(llm_output)
            
            self._tool_call_validator.validate(tool_call)
            
            tool = self._tool_registry.get(
                tool_call.tool_name
            )
            
            tool_output = tool.execute(
                tool_call.arguments
            )
            
            self._memory.add_message(tool_output)
            
            history = self._memory.get_history()
        
        return Response(output=tool_output)