from .base_llm import BaseLLM
from collections.abc import Iterator


class MockLLM(BaseLLM):
    
    def generate(self, prompt: str) -> str:
        return f"Mock response: {prompt}"

    
    def stream(self, prompt: str) -> Iterator[str]:
        response = self.generate(prompt)
        
        for word in response.split():
            yield word + " "