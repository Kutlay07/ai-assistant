from ai_assistant.core.models import Chunk
from ai_assistant.core.vector_stores import MockVectorStore


def test_add_stores_chunks():

    store = MockVectorStore()

    chunks = [
        Chunk(content="Chunk 1"),
        Chunk(content="Chunk 2"),
    ]

    store.add(chunks)

    results = store.search([])

    assert len(results) == 2


def test_search_returns_chunks():

    store = MockVectorStore()

    chunks = [
        Chunk(content="Chunk 1"),
        Chunk(content="Chunk 2"),
    ]

    store.add(chunks)

    results = store.search([])

    assert results == chunks


def test_search_respects_top_k():

    store = MockVectorStore()

    chunks = [
        Chunk(content="Chunk 1"),
        Chunk(content="Chunk 2"),
        Chunk(content="Chunk 3"),
    ]

    store.add(chunks)

    results = store.search([], top_k=2)

    assert len(results) == 2


def test_empty_store_returns_empty_list():

    store = MockVectorStore()

    results = store.search([])

    assert results == []