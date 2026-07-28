from dataclasses import dataclass


@dataclass(slots=True)
class Chunk:
    content: str
    embedding: list[float] | None = None