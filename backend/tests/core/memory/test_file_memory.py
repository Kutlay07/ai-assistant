from ai_assistant.core.memory import FileMemory


def test_new_file_returns_empty_history(tmp_path):
    path = tmp_path / "conversation.json"

    memory = FileMemory(path)

    assert memory.get_history() == []


def test_add_message(tmp_path):
    path = tmp_path / "conversation.json"

    memory = FileMemory(path)
    
    memory.add_message("Hello")

    assert memory.get_history() == [
        "Hello",
    ]


def test_history_persists_between_instances(tmp_path):
    path = tmp_path / "conversation.json"

    memory1 = FileMemory(path)

    memory1.add_message("Hello")

    memory2 = FileMemory(path)

    assert memory2.get_history() == [
        "Hello",
    ]


def test_multiple_messages(tmp_path):
    path = tmp_path / "conversation.json"

    memory = FileMemory(path)

    memory.add_message("Hello")
    memory.add_message("Hi")
    memory.add_message("How are you?")

    assert memory.get_history() == [
        "Hello",
        "Hi",
        "How are you?",
    ]