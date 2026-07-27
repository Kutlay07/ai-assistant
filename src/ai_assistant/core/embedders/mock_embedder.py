from .base_embedder import BaseEmbedder


class MockEmbedder(BaseEmbedder):

    def embed(self, text: str) -> list[float]:
        return [
            float(len(text)),
            float(sum(text.encode())),
            float(len(set(text))),
        ]