from sentence_transformers import SentenceTransformer

from .base_embedder import BaseEmbedder


class SentenceTransformerEmbedder(BaseEmbedder):
    
    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ):
        self._model = SentenceTransformer(model_name)
        
    def embed(self, text: str) -> list[float]:
        embedding = self._model.encode(
            text,
            convert_to_numpy=True,
        )
        
        return embedding.tolist()