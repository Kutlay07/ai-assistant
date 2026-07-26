from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Response:
    """Represents the assistant's response"""
    output: str