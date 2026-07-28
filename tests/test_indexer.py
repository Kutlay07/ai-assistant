from ai_assistant.core.indexer import Indexer
from ai_assistant.core.loaders import TextLoader
from ai_assistant.core.splitters import TextSplitter
from ai_assistant.core.embedders import MockEmbedder
from ai_assistant.core.vector_stores import MockVectorStore

import pytest


def test_index_adds_chunks_to_vector_store(tmp_path):

    file = tmp_path / "sample.txt"
    file.write_text("Hello World", encoding="utf-8")

    vector_store = MockVectorStore()

    indexer = Indexer(
        loader=TextLoader(),
        splitter=TextSplitter(),
        embedder=MockEmbedder(),
        vector_store=vector_store,
    )

    indexer.index(file)

    chunks = vector_store.search(
        embedding=[],
        top_k=10,
    )

    assert len(chunks) == 1


def test_index_generates_embeddings(tmp_path):

    file = tmp_path / "sample.txt"
    file.write_text("Hello World", encoding="utf-8")

    vector_store = MockVectorStore()

    indexer = Indexer(
        loader=TextLoader(),
        splitter=TextSplitter(),
        embedder=MockEmbedder(),
        vector_store=vector_store,
    )

    indexer.index(file)

    chunk = vector_store.search(
        embedding=[],
        top_k=1,
    )[0]

    assert chunk.embedding is not None


def test_index_missing_file_raises_error():

    indexer = Indexer(
        loader=TextLoader(),
        splitter=TextSplitter(),
        embedder=MockEmbedder(),
        vector_store=MockVectorStore(),
    )

    with pytest.raises(FileNotFoundError):
        indexer.index("missing.txt")


def test_index_preserves_chunk_content(tmp_path):

    file = tmp_path / "sample.txt"
    file.write_text("Hello World", encoding="utf-8")

    vector_store = MockVectorStore()

    indexer = Indexer(
        loader=TextLoader(),
        splitter=TextSplitter(),
        embedder=MockEmbedder(),
        vector_store=vector_store,
    )

    indexer.index(file)

    chunk = vector_store.search(
        embedding=[],
        top_k=1,
    )[0]

    assert chunk.content == "Hello World"