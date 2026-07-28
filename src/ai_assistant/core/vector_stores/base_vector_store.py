from abc import ABC, abstractmethod

from ..models import Chunk


class BaseVectorStore(ABC):
    
    @abstractmethod
    def add(self, chunks: list[Chunk]) -> None:
        pass
    
    @abstractmethod
    def search(self, 
            embedding: list[float],
            top_k: int=5,) -> list[Chunk]:
        pass