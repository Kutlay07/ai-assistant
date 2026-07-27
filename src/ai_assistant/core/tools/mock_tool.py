from .base_tool import BaseTool


class MockTool(BaseTool):
    
    def execute(self, query: str) -> str:
        return f"Mock tool response: {query}"