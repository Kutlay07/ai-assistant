from ..models import Chunk
from ..models import Chunk, RetrievalOptions

from abc import ABC, abstractmethod


class BaseRetriever(ABC):
    
    @abstractmethod
    def retrieve(
        self,
        query: str,
        options: RetrievalOptions | None = None,
    ) -> list[Chunk]:
        
        pass