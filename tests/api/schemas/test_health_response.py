from ai_assistant.api.schemas import HealthResponse


def test_health_response_accepts_valid_status():
    health = HealthResponse(status="ok")

    assert health.status == "ok"