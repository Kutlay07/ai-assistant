from dataclasses import dataclass


@dataclass(slots=True)
class RetrievalOptions:
    top_k: int = 5