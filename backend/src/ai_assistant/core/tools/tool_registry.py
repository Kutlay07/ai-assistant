from .base_tool import BaseTool


class ToolRegistry:
    
    def __init__(self):
        self._tools: dict[str, BaseTool] = {}
        
    
    def register(self, tool: BaseTool) -> None:

        if tool.name in self._tools:
            raise ValueError(
                f"Tool '{tool.name}' is already registered."
            )
            
        self._tools[tool.name] = tool
        
    
    def get(self, name: str) -> BaseTool:
        try:
            return self._tools[name]
        except KeyError as e:
            raise ValueError(f"Tool '{name}' is not registered.") from e

    
    def list(self) -> list[str]:
        return list(self._tools.keys())