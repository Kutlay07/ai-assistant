from abc import ABC, abstractmethod
from collections.abc import Sequence

from ..models import Chunk, RetrievalOptions


class BaseSearchService(ABC):
    
    @abstractmethod
    def search(
        self,
        query: str,
        options: RetrievalOptions | None = None,
    ) -> Sequence[Chunk]:
        
        pass