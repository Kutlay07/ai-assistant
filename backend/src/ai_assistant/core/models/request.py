from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Request:
    """Represents a user request sent to the AI Assistant"""
    input: str

