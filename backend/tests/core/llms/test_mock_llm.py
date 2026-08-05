from ai_assistant.core.llms import BaseLLM, MockLLM


def test_mock_llm_generates_response():
    llm = MockLLM()

    response = llm.generate("Hello")

    assert response == "Mock response: Hello"


def test_mock_llm_is_base_llm():
    llm = MockLLM()

    assert isinstance(llm, BaseLLM)