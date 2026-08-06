import json
from unittest.mock import MagicMock

from ai_assistant.core.memory.redis_memory import RedisMemory


def test_add_message_stores_message():
    memory = RedisMemory(client=MagicMock())
    
    memory.client = MagicMock()

    memory.client.get.return_value = None

    memory.add_message(
        "user",
        "hello",
    )

    memory.client.set.assert_called_once_with(
        "conversation",
        json.dumps(
            [
                {
                    "role": "user",
                    "content": "hello",
                }
            ]
        ),
        ex=3600,
    )


def test_get_history_returns_messages():
    
    memory = RedisMemory(client=MagicMock())
    
    memory.client = MagicMock()

    messages = [
        {
            "role": "assistant",
            "content": "hi",
        }
    ]

    memory.client.get.return_value = json.dumps(messages)

    result = memory.get_history()

    assert result == messages


def test_get_history_returns_empty_when_missing():
    memory = RedisMemory(client=MagicMock())
    
    memory.client = MagicMock()

    memory.client.get.return_value = None

    result = memory.get_history()

    assert result == []