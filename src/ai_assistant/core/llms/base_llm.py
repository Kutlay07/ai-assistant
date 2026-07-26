from abc import ABC, abstractmethod


class BaseLLM(ABC):
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the given prompt"""
        pass