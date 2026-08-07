import hashlib

from .base_embedder import BaseEmbedder
from ..cache.base_cache import BaseCache


class MockEmbedder(BaseEmbedder):

    def __init__(
        self,
        cache: BaseCache | None = None,
    ):
        self.cache = cache

    def embed(self, text: str):
        key = "embedding:" + hashlib.sha256(
            text.encode()
        ).hexdigest()

        if self.cache is not None:
            cached = self.cache.get(key)

            if cached is not None:
                return cached

        embedding = [
            float(len(text)),
            float(sum(text.encode())),
            float(len(set(text))),
        ]

        if self.cache is not None:
            self.cache.set(key, embedding)

        return embedding