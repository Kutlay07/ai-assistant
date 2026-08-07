from unittest.mock import MagicMock

from ai_assistant.core.cache.redis_cache import RedisCache


def test_set_and_get():
    client = MagicMock()

    cache = RedisCache(client=client)

    value = {
        "text": "hello",
        "score": 0.95,
    }

    cache.set("embedding", value)

    client.get.return_value = '{"text": "hello", "score": 0.95}'

    result = cache.get("embedding")

    client.set.assert_called_once_with(
    "embedding",
    '{"text": "hello", "score": 0.95}',
    ex=3600,
    )


def test_get_returns_none_when_key_missing():
    client = MagicMock()

    cache = RedisCache(client=client)

    client.get.return_value = None

    assert cache.get("missing") is None


def test_delete_key():
    client = MagicMock()

    cache = RedisCache(client=client)

    cache.delete("embedding")

    client.delete.assert_called_once_with("embedding")


def test_clear_cache():
    client = MagicMock()

    cache = RedisCache(client=client)

    cache.clear()

    client.flushdb.assert_called_once()