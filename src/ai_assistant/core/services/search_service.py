from ..retrievers import BaseRetriever
from ..models import RetrievalOptions
from .base_search_service import BaseSearchService

class SearchService(BaseSearchService):
    """Application service for semantic search"""
    def __init__(self, retriever: BaseRetriever):
        self._retriever = retriever
        
        
    def search(
        self,
        query: str,
        options: RetrievalOptions | None = None,
        ):
        
        return self._retriever.retrieve(
            query=query,
            options=options,
        )