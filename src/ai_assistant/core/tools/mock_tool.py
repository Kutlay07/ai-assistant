from .base_tool import BaseTool


class MockTool(BaseTool):
    
    def execute(self, input: str) -> str:
        return f"Mock tool response: {input}"