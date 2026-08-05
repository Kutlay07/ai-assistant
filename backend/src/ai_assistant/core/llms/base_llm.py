from abc import ABC, abstractmethod
from collections.abc import Iterator


class BaseLLM(ABC):
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the given prompt"""
        pass
    
    @abstractmethod
    def stream(self, prompt: str) -> Iterator[str]:
        """Stream a response from the given prompt"""
        pass