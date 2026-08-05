from dataclasses import dataclass


@dataclass(frozen=True)
class ToolSelection:
    tool_name: str
    query: str