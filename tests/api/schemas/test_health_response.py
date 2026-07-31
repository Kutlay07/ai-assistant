from ai_assistant.api.schemas import HealthResponse


health = HealthResponse(status="ok")

assert health.status == "ok"