from ..retrievers import BaseRetriever
from ..models import RetrievalOptions
from .base_search_service import BaseSearchService
from typing import Sequence
from ..models import Chunk

class SearchService(BaseSearchService):
    """Application service for semantic search"""
    def __init__(self, retriever: BaseRetriever):
        self._retriever = retriever
        
        
    def search(
        self,
        query: str,
        options: RetrievalOptions | None = None,
        ) -> Sequence[Chunk]:
        
        return self._retriever.retrieve(
            query=query,
            options=options,
        )