from ..retrievers import BaseRetriever
from ..models import Chunk

class SearchService:
    """Application service for semantic search"""
    def __init__(self, retriever: BaseRetriever):
        self._retriever = retriever
        
    def search(self, query: str, top_k: int=5) -> list[Chunk]:
        """Retrieve the most relevant document chunks"""
        return self._retriever.retrieve(
            query=query,
            top_k=top_k
        )