import pytest

from ai_assistant.core.models import Response


def test_response_stores_output():
    response = Response(output="Hello")

    assert response.output == "Hello"


def test_response_is_immutable():
    response = Response(output="Hello")

    with pytest.raises(AttributeError):
        response.output = "Hi"