from ai_assistant.core.memory import MockMemory


def test_mock_memory_returns_empty_history():
    memory = MockMemory()

    assert memory.get_history() == []


def test_mock_memory_stores_messages():
    memory = MockMemory()

    memory.add_message("user","Hello")

    assert memory.get_history() == [
        {
            "role": "user",
            "content": "Hello",
        }
    ]


def test_mock_memory_preserves_message_order():
    memory = MockMemory()

    memory.add_message("user", "Hello")
    memory.add_message("user", "How are you?")

    assert memory.get_history() == [
        {
            "role": "user",
            "content": "Hello",
        },
        {
            "role": "user",
            "content": "How are you?",
        },
    ]