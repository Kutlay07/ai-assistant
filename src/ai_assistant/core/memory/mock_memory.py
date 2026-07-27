from .base_memory import BaseMemory


class MockMemory(BaseMemory):
    
    def __init__(self):
        self._messages = []
        
    def get_history(self) -> list[str]:
        return self._messages
    
    def add_message(self, message: str) -> None:
        self._messages.append(message)