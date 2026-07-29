from abc import ABC, abstractmethod

from ..models import Chunk, RetrievalOptions


class BaseSearchService(ABC):
    
    @abstractmethod
    def search(
        self,
        query: str,
        options: RetrievalOptions | None = None,
    ) -> list[Chunk]:
        
        pass