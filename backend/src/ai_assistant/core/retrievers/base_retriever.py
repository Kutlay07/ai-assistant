from ..models import Chunk, RetrievalOptions
from collections.abc import Sequence

from abc import ABC, abstractmethod


class BaseRetriever(ABC):
    
    @abstractmethod
    def retrieve(
        self,
        query: str,
        options: RetrievalOptions | None = None,
    ) -> Sequence[Chunk]:
        
        pass