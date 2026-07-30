from fastapi.testclient import TestClient

from ai_assistant.api import app

client = TestClient(app)


def test_chat_returns_response():
    response = client.post(
        "/chat",
        json={
            "message":"Hello",
            },
        )
    assert response.status_code == 200
    assert "Hello" in response.json()["response"]


def test_chat_stream():
    with client.stream(
        "POST",
        "/chat/stream",
        json={"message": "Hello"},
    ) as response:
        assert response.status_code == 200

        output = "".join(response.iter_text())

        assert "Mock response" in output