from ai_assistant.core.embedders import MockEmbedder
from ai_assistant.core.models import Chunk
from ai_assistant.core.retrievers import MockRetriever
from ai_assistant.core.vector_stores import MockVectorStore


def test_retrieve_returns_chunks():

    embedder = MockEmbedder()
    vector_store = MockVectorStore()

    chunks = [
        Chunk(content="Chunk 1"),
        Chunk(content="Chunk 2"),
    ]

    vector_store.add(chunks)

    retriever = MockRetriever(
        embedder=embedder,
        vector_store=vector_store,
    )

    results = retriever.retrieve("Hello")

    assert results == chunks

def test_retrieve_respects_top_k():

    embedder = MockEmbedder()
    vector_store = MockVectorStore()

    chunks = [
        Chunk(content="Chunk 1"),
        Chunk(content="Chunk 2"),
        Chunk(content="Chunk 3"),
    ]

    vector_store.add(chunks)

    retriever = MockRetriever(
        embedder=embedder,
        vector_store=vector_store,
    )

    results = retriever.retrieve(
        "Hello",
        top_k=2,
    )

    assert len(results) == 2


def test_retrieve_empty_store_returns_empty_list():

    retriever = MockRetriever(
        embedder=MockEmbedder(),
        vector_store=MockVectorStore(),
    )

    results = retriever.retrieve("Hello")

    assert results == []


def test_retrieve_uses_embedder():

    embedder = MockEmbedder()
    vector_store = MockVectorStore()

    vector_store.add([
        Chunk(content="Chunk"),
    ])

    retriever = MockRetriever(
        embedder=embedder,
        vector_store=vector_store,
    )

    results = retriever.retrieve("Hello")

    assert isinstance(results, list)