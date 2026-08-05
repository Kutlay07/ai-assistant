from ai_assistant.core.models import Request, Response, ToolCall
from ai_assistant.core.workflows import BaseWorkflow
from ai_assistant.core.tools import ToolRegistry, ToolCallValidator


class Assistant:
    """Coordinates request execution through a workflow"""
    
    def __init__(
        self, 
        workflow: BaseWorkflow, 
        tool_registry: ToolRegistry,
        ):
        self._workflow = workflow
        self._tool_registry = tool_registry
        
    def execute_tool(self, tool_call: ToolCall,) -> str:
        validator = ToolCallValidator()
        
        validator.validate(tool_call)
        
        tool = self._tool_registry.get(tool_call.tool_name)
        
        return tool.execute(tool_call.arguments)
    
    def handle(self, request: Request) -> Response:
        return self._workflow.run(request)
    
    def stream(self, request: Request):
        return self._workflow.stream(request)