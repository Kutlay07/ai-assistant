from fastapi.testclient import TestClient

from main import app
from ai_assistant.api.constants import API_PREFIX


client = TestClient(app)


def test_rag_endpoint_returns_retrieved_context():
    response = client.post(
        f"{API_PREFIX}/rag",
        json={
            "message": "What is RAG?",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "response" in body
    assert "RAG combines retrieval with language models." in body["response"]