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
        
        
    def _load_messages(self) -> list[dict[str, str]]:
        if not self._path.exists():
            return []

        with self._path.open("r", encoding="utf-8") as file:
            try:
                messages = json.load(file)
            except json.JSONDecodeError:
                return []

        if not isinstance(messages, list):
            return []

        if messages and isinstance(messages[0], str):
            messages = [
                {
                    "role": "user" if index % 2 == 0 else "assistant",
                    "content": message,
                }
                for index, message in enumerate(messages)
            ]

            self._save_messages(messages)

        return messages
        
        
    def _save_messages(self, messages: list[dict[str, str]]):
        with self._path.open("w", encoding="utf-8",) as file:
            json.dump(
                messages,
                file,
                indent=4,
                ensure_ascii=False,
            )
        
    def get_history(self) -> list[dict[str, str]]:
        return self._load_messages()
        
        
    def get_messages(self) -> list[dict[str, str]]:
        return self._load_messages()
        
    def add_message(self, role: str, content: str) -> None:
        messages = self._load_messages()
        
        messages.append(
            {
                "role": role,
                "content": content,
            }
        )
        
        self._save_messages(messages)