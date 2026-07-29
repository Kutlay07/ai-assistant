from .base_tool import BaseTool
from collections.abc import Mapping
from typing import Any


class MockTool(BaseTool):
    
    @property
    def name(self) -> str:
        return "mock"

    
    def execute(self, arguments: Mapping[str, Any]) -> str:
        return f"Mock tool response: {arguments['query']}"