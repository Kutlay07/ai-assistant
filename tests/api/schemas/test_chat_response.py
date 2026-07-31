from ai_assistant.api.schemas import ChatResponse


def test_chat_response_accepts_valid_response():
    response = ChatResponse(response="Hi")

    assert response.response == "Hi"