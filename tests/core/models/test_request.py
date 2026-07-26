from ai_assistant.core.models import Request
import pytest


def test_request_stores_input():
    request = Request(input="Hello")

    assert request.input == "Hello"
    


def test_request_is_immutable():
    request = Request(input="Hello")

    with pytest.raises(AttributeError):
        request.input = "Hi"