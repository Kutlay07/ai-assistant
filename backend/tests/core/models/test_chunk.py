from ai_assistant.core.models import Chunk


def test_chunk_stores_content():

    chunk = Chunk(content="Hello")

    assert chunk.content == "Hello"