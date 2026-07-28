from .loaders import BaseLoader
from .embedders import BaseEmbedder
from .vector_stores import BaseVectorStore
from .splitters import BaseSplitter

from pathlib import Path
from collections.abc import Iterable



class Indexer:

    def __init__(
        self,
        loader: BaseLoader,
        splitter: BaseSplitter,
        embedder: BaseEmbedder,
        vector_store: BaseVectorStore,
    ):
        self._loader = loader
        self._splitter = splitter
        self._embedder = embedder
        self._vector_store = vector_store
        
    
    def index(self, path: str | Path) -> None:
        document = self._loader.load(path)
        
        chunks = self._splitter.split(document)
        
        for chunk in chunks:
            chunk.embedding = self._embedder.embed(chunk.content)

        self._vector_store.add(chunks)
        
        
    def index_batch(self, paths: Iterable[str | Path]) -> None:
        for path in paths:
            self.index(path)