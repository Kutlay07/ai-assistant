from .base_tool import BaseTool


class MockTool(BaseTool):
    
    @property
    def name(self) -> str:
        return "mock"

    
    def execute(self, arguments: dict[str, str]) -> str:
        return f"Mock tool response: {arguments['query']}"