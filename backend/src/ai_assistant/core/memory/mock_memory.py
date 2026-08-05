from .base_memory import BaseMemory


class MockMemory(BaseMemory):
    
    def __init__(self):
        self._messages = []
        
    def get_history(self) -> list[dict[str, str]]:
        return self._messages.copy()
    
    def add_message(self, role: str, content: str) -> None:
        self._messages.append(
            {
                "role": role,
                "content": content,
            }
        )