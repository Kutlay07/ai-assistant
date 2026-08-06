import json

import redis

from .base_memory import BaseMemory


class RedisMemory(BaseMemory):
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        ttl: int = 3600,
        key: str = "conversation",
    ):
        self.client = redis.Redis(
            host=host,
            port=port,
            decode_responses=True,
        )

        self.ttl = ttl
        self.key = key


    def get_history(self) -> list[dict[str, str]]:
        data = self.client.get(self.key)

        if data is None:
            return []

        return json.loads(data)


    def add_message(
        self,
        role: str,
        content: str,
    ) -> None:
        history = self.get_history()

        history.append(
            {
                "role": role,
                "content": content,
            }
        )

        self.client.set(
            self.key,
            json.dumps(history),
            ex=self.ttl,
        )