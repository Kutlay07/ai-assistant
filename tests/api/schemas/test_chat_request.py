import pytest
from pydantic import ValidationError

from ai_assistant.api.schemas import ChatRequest


def test_chat_request_accepts_valid_message():
    request = ChatRequest(message="Hello")

    assert request.message == "Hello"


def test_chat_request_rejects_empty_message():
    with pytest.raises(ValidationError):
        ChatRequest(message="")


def test_chat_request_rejects_long_message():
    with pytest.raises(ValidationError):
        ChatRequest(message="a" * 1001)