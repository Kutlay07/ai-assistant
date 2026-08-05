from fastapi.testclient import TestClient

from ai_assistant.api.main import app


client = TestClient(app)


def test_rag_endpoint_returns_retrieved_context():
    response = client.post(
        "/rag",
        json={
            "message": "What is RAG?",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "response" in body
    assert "RAG combines retrieval with language models." in body["response"]