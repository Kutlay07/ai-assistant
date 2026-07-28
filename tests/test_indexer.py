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


def test_index_batch_indexes_multiple_documents(tmp_path):

    file1 = tmp_path / "sample1.txt"
    file1.write_text("Hello", encoding="utf-8")

    file2 = tmp_path / "sample2.txt"
    file2.write_text("World", encoding="utf-8")

    vector_store = MockVectorStore()

    indexer = Indexer(
        loader=TextLoader(),
        splitter=TextSplitter(),
        embedder=MockEmbedder(),
        vector_store=vector_store,
    )

    indexer.index_batch([file1, file2])

    assert len(vector_store.search([], top_k=100)) == 2


def test_index_batch_preserves_document_metadata(tmp_path):

    file = tmp_path / "sample.txt"
    file.write_text("Hello World", encoding="utf-8")

    vector_store = MockVectorStore()

    indexer = Indexer(
        loader=TextLoader(),
        splitter=TextSplitter(),
        embedder=MockEmbedder(),
        vector_store=vector_store,
    )

    indexer.index_batch([file])

    chunk = vector_store.search([], top_k=1)[0]

    assert chunk.document is not None
    assert chunk.document.title == "sample"
    assert chunk.document.source.endswith("sample.txt")


def test_index_batch_empty_list():

    vector_store = MockVectorStore()

    indexer = Indexer(
        loader=TextLoader(),
        splitter=TextSplitter(),
        embedder=MockEmbedder(),
        vector_store=vector_store,
    )

    indexer.index_batch([])

    assert vector_store.search([], top_k=100) == []