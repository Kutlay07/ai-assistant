from dataclasses import dataclass

from .document import Document


@dataclass(slots=True)
class Chunk:
    content: str
    embedding: list[float] | None = None
    document: Document | None = None