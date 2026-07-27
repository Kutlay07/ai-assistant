from abc import ABC, abstractmethod


class BaseMemory(ABC):
    
    @abstractmethod
    def get_history(self) -> list[str]:
        pass
    
    @abstractmethod
    def add_message(self, message: str) -> None:
        pass