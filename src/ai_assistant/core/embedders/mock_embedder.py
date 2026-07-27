from .base_embedder import BaseEmbedder


class MockEmbedder(BaseEmbedder):

    def embed(self, text: str) -> list[float]:
        return [0.1, 0.2, 0.3]