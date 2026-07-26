from ai_assistant.core.llms import BaseLLM


class DummyLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        return "dummy"
    

def test_base_llm_generate():
    llm = DummyLLM()
    
    response = llm.generate("Hello")
    
    assert response == "dummy"


def test_base_llm_is_instantiable_through_subclass():
    llm = DummyLLM()
    
    assert isinstance(llm, BaseLLM)