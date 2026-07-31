from ai_assistant.api.schemas import ChatResponse

response = ChatResponse(response="Hi")

assert response.response == "Hi"