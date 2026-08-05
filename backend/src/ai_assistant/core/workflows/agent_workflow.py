from collections.abc import Callable

from ..models import Request, Response, ToolCall
from .base_workflow import BaseWorkflow
from ..llms import BaseLLM
from ..memory import BaseMemory
from ..prompts import PromptBuilder
from ..planners import BasePlanner
from ..parsers import ToolCallParser


class AgentWorkflow(BaseWorkflow):
    """Workflow for agent-based interactions"""
    
    def __init__(
        self,
        llm: BaseLLM, 
        prompt_builder: PromptBuilder, 
        memory: BaseMemory,
        planner: BasePlanner,
        tool_call_parser: ToolCallParser,
        execute_tool: Callable[[ToolCall], str] | None = None,
        max_iterations: int = 3,
        ):
        super().__init__()
        
        self._llm = llm
        self._prompt_builder = prompt_builder
        self._memory = memory
        self._planner = planner
        self._tool_call_parser = tool_call_parser
        self._execute_tool = execute_tool
        self._max_iterations = max_iterations
        
        if max_iterations < 1:
            raise ValueError(
                "max_iterations must be greater than 0."
            )
        
    def set_execute_tool(
        self,
        execute_tool: Callable[[ToolCall], str],
        ) -> None:
        self._execute_tool = execute_tool
        
    def run(self, request: Request) -> Response:
        if self._execute_tool is None:
            raise RuntimeError(
                "Tool executor is not configured."
            )
            
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
            
            tool_call = self._tool_call_parser.parse(
                llm_output
            )
            
            tool_output = self._execute_tool(tool_call)
            
            self._memory.add_message(tool_output)
            
            history = self._memory.get_history()
        
        return Response(output=tool_output)