from ai_assistant.core.memory.mock_memory import MockMemory

def test_mock_memory_returns_empty_history():

    memory = MockMemory()

    assert memory.get_history() == []
    
def test_mock_memory_preserves_message_order():
    memory = MockMemory()

    memory.add_message("Hello")
    memory.add_message("How are you?")

    assert memory.get_history() == [
        "Hello",
        "How are you?",
    ]
    
def test_mock_memory_stores_messages():

    memory = MockMemory()

    memory.add_message("Hello")

    assert memory.get_history() == ["Hello"]
    
    
