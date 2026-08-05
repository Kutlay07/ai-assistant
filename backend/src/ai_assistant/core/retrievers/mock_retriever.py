from ..embedders import BaseEmbedder
from ..models import Chunk
from ..vector_stores import BaseVectorStore
from ..models import RetrievalOptions
from .base_retriever import BaseRetriever


class MockRetriever(BaseRetriever):
    
    def __init__(self,
                embedder: BaseEmbedder, 
                vector_store: BaseVectorStore,
                ):
        self.embedder = embedder
        self.vector_store = vector_store
        
        
    def retrieve(
        self,
        query: str,
        options: RetrievalOptions | None = None,
        ) -> list[Chunk]:

        if options is None:
            options = RetrievalOptions()

        embedding = self.embedder.embed(query)

        return self.vector_store.search(
            embedding=embedding,
            top_k=options.top_k,
        )