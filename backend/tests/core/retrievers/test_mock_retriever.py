from unittest.mock import MagicMock

from ai_assistant.core.models import Chunk
from ai_assistant.core.retrievers.mock_retriever import MockRetriever


def test_retrieve_cache_miss():
    embedder = MagicMock()
    vector_store = MagicMock()
    cache = MagicMock()

    cache.get.return_value = None

    embedder.embed.return_value = [1.0, 2.0]

    chunks = [
        Chunk(content="chunk 1"),
        Chunk(content="chunk 2"),
    ]

    vector_store.search.return_value = chunks

    retriever = MockRetriever(
        embedder=embedder,
        vector_store=vector_store,
        cache=cache,
    )

    result = retriever.retrieve("hello")

    assert result == chunks

    embedder.embed.assert_called_once_with("hello")
    vector_store.search.assert_called_once()
    cache.set.assert_called_once()


def test_retrieve_cache_hit():
    embedder = MagicMock()
    vector_store = MagicMock()
    cache = MagicMock()

    cache.get.return_value = [
        {
            "content": "cached",
            "embedding": None,
            "document": None,
        }
    ]

    retriever = MockRetriever(
        embedder=embedder,
        vector_store=vector_store,
        cache=cache,
    )

    result = retriever.retrieve("hello")

    assert len(result) == 1
    assert result[0].content == "cached"

    embedder.embed.assert_not_called()
    vector_store.search.assert_not_called()
    cache.set.assert_not_called()


def test_retrieve_without_cache():
    embedder = MagicMock()
    vector_store = MagicMock()

    embedder.embed.return_value = [1.0]

    chunks = [
        Chunk(content="chunk"),
    ]

    vector_store.search.return_value = chunks

    retriever = MockRetriever(
        embedder=embedder,
        vector_store=vector_store,
    )

    result = retriever.retrieve("hello")

    assert result == chunks

    embedder.embed.assert_called_once()
    vector_store.search.assert_called_once()