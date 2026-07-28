from ..retrievers import BaseRetriever
from ..models import Chunk
from ..models import RetrievalOptions

class SearchService:
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