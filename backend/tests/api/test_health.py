from fastapi.testclient import TestClient

from main import app
from ai_assistant.api.constants import API_PREFIX

client = TestClient(app)


def test_health_endpoint_returns_ok():
    response = client.get(f"{API_PREFIX}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}