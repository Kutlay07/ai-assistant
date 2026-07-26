from .base_llm import BaseLLM


class MockLLM(BaseLLM):
    
    def generate(self, prompt: str) -> str:
        return f"Mock response: {prompt}"