import pytest
from fastapi.testclient import TestClient

from main import app
from ai_assistant.api.constants import API_PREFIX
from ai_assistant.api.dependencies import get_assistant
from ai_assistant.core.llms.mock_llm import MockLLM
from ai_assistant.core.assistant import Assistant


class MockAssistant(Assistant):
    def __init__(self):
        self.llm = MockLLM()

    def handle(self, request):
        return type(
            "Response",
            (),
            {"output": "Mock response"},
        )()

    def stream(self, request):
        yield "Mock streaming response"


@pytest.fixture
def client():
    app.dependency_overrides[get_assistant] = lambda: MockAssistant()

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


def test_chat_returns_response(client):
    response = client.post(
        f"{API_PREFIX}/chat",
        json={
            "message": "Hello",
        },
    )

    assert response.status_code == 200
    assert "response" in response.json()


def test_chat_stream(client):
    with client.stream(
        "POST",
        f"{API_PREFIX}/chat/stream",
        json={
            "message": "Hello",
        },
    ) as response:

        assert response.status_code == 200

        assert response.headers["content-type"].startswith(
            "text/plain"
        )

        output = "".join(response.iter_text())

        assert output.strip() != ""


def test_chat_rejects_empty_message(client):
    response = client.post(
        f"{API_PREFIX}/chat",
        json={
            "message": "",
        },
    )

    assert response.status_code == 422


def test_stream_rejects_empty_message(client):
    response = client.post(
        f"{API_PREFIX}/chat/stream",
        json={
            "message": "",
        },
    )

    assert response.status_code == 422