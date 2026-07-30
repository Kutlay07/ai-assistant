from fastapi.testclient import TestClient

from ai_assistant.api import app

client = TestClient(app)


def test_health_returns_response():
    response = client.post(
        "/chat",
        json={
            "message":"Hello",
            },
        )
    assert response.status_code == 200
    assert "Hello" in response.json()["response"]