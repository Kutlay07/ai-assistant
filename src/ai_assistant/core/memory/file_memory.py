import json
from pathlib import Path

from .base_memory import BaseMemory


class FileMemory(BaseMemory):
    
    def __init__(self, path: Path):
        self._path = path
        
        self._path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        
        
    def _load_messages(self) -> list[str]:
        if not self._path.exists():
            return []
        
        with self._path.open("r", encoding="utf-8") as file:
            return json.load(file)
        
        
    def _save_messages(self, messages: list[str]):
        with self._path.open("w", encoding="utf-8",) as file:
            json.dump(
                messages,
                file,
                indent=4,
                ensure_ascii=False,
            )
        
    def get_history(self) -> list[str]:
        return self._load_messages()
        
        
    def add_message(self, message: str) -> None:
        messages = self._load_messages()
        
        messages.append(message)
        
        self._save_messages(messages)