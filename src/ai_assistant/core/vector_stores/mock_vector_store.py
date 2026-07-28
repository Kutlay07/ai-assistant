from ..models import Chunk

from .base_vector_store import BaseVectorStore


class MockVectorStore(BaseVectorStore):
    
    def __init__(self):
        self._chunks: list[Chunk] = []
        
    
    def add(self, chunks: list[Chunk]) -> None:
        self._chunks.extend(chunks)
        
        
    def search(self, 
            embedding: list[float],
            top_k: int=5) -> list[Chunk]:
        
        return self._chunks[:top_k]