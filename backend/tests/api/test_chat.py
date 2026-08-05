from fastapi.testclient import TestClient

from main import app
from ai_assistant.api.constants import API_PREFIX

client = TestClient(app)


def test_chat_returns_response():
    response = client.post(
        f"{API_PREFIX}/chat",
        json={
            "message":"Hello",
            },
        )
    assert response.status_code == 200
    assert "response" in response.json()


def test_chat_stream():
    with client.stream(
        "POST",
        f"{API_PREFIX}/chat/stream",
        json={"message": "Hello"},
    ) as response:
        assert response.status_code == 200
        
        assert response.headers["content-type"].startswith("text/plain")

        output = "".join(response.iter_text())

        assert output.strip() != ""


def test_chat_rejects_empty_message():
    response = client.post(
        f"{API_PREFIX}/chat",
        json={
            "message": "",
        },
    )

    assert response.status_code == 422


def test_stream_rejects_empty_message():
    response = client.post(
        f"{API_PREFIX}/chat/stream",
        json={
            "message": "",
        },
    )

    assert response.status_code == 422