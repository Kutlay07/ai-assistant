from abc import ABC, abstractmethod

from ..models import Chunk


class BaseRetriever(ABC):
    
    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int=5,
    ) -> list[Chunk]:
        
        pass