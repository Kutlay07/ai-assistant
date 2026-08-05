from abc import ABC, abstractmethod


class BaseMemory(ABC):
    """Abstract interface for conversation memory implementations"""
    @abstractmethod
    def get_history(self) -> list[str]:
        """Return the stored conversation history"""
        pass
    
    @abstractmethod
    def add_message(self, message: str) -> None:
        """Store a conversation message"""
        pass