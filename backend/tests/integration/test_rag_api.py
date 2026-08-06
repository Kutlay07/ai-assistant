import pytest
from fastapi.testclient import TestClient

from main import app
from ai_assistant.api.constants import API_PREFIX
from ai_assistant.api.dependencies import get_rag_assistant


class MockRAGAssistant:

    def handle(self, request):
        return type(
            "Response",
            (),
            {
                "output": (
                    "RAG combines retrieval with language models."
                )
            },
        )()


@pytest.fixture
def client():
    app.dependency_overrides[get_rag_assistant] = (
        lambda: MockRAGAssistant()
    )

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_rag_endpoint_returns_retrieved_context(client):

    response = client.post(
        f"{API_PREFIX}/rag",
        json={
            "message": "What is RAG?",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "response" in body
    assert (
        "RAG combines retrieval with language models."
        in body["response"]
    )