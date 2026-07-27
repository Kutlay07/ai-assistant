from ai_assistant.core.embedders import MockEmbedder


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