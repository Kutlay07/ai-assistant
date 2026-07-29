from dataclasses import dataclass


@dataclass(frozen=True)
class ToolCall:
    tool_name: str
    arguments: dict[str, str]