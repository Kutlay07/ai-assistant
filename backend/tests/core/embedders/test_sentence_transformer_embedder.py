from ai_assistant.core.embedders import (
    SentenceTransformerEmbedder,
)


def test_sentence_transformer_embedder_returns_vector():

    embedder = SentenceTransformerEmbedder()

    embedding = embedder.embed(
        "Redis is an in-memory database."
    )

    assert isinstance(embedding, list)
    assert len(embedding) > 0
    assert all(
        isinstance(value, float)
        for value in embedding
    )