from unittest.mock import MagicMock

from ai_assistant.core.embedders import MockEmbedder
from ai_assistant.core.cache import RedisCache


def test_mock_embedder_returns_list():

    embedder = MockEmbedder()

    embedding = embedder.embed("Hello")

    assert isinstance(embedding, list)


def test_mock_embedder_returns_floats():

    embedder = MockEmbedder()

    embedding = embedder.embed("Hello")

    assert all(isinstance(value, float) for value in embedding)


def test_mock_embedder_is_deterministic():

    embedder = MockEmbedder()

    assert embedder.embed("Hello") == embedder.embed("Hello")


def test_embedder_caches_embedding():
    client = MagicMock()

    cache = RedisCache(client=client)
    embedder = MockEmbedder(cache=cache)

    client.get.return_value = None

    result = embedder.embed("hello")

    client.set.assert_called_once()

    assert result == [
        5.0,
        float(sum("hello".encode())),
        float(len(set("hello"))),
    ]


def test_embedder_returns_cached_embedding():
    client = MagicMock()

    cache = RedisCache(client=client)
    embedder = MockEmbedder(cache=cache)

    client.get.return_value = "[1.0, 2.0, 3.0]"

    result = embedder.embed("hello")

    assert result == [1.0, 2.0, 3.0]

    client.set.assert_not_called()