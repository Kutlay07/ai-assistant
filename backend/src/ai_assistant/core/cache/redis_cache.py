import json

import redis

from .base_cache import BaseCache


class RedisCache(BaseCache):
    
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        ttl: int = 3600,
        client: redis.Redis | None = None,
        ):
        
        self.client = (
            client
            if client is not None
            else redis.Redis(
                host=host,
                port=port,
                decode_responses=True,
            )
        )
        
        self.ttl = ttl
        
    def set(
        self,
        key: str,
        value,
        ttl: int | None = None,
    ):
        ttl = ttl if ttl is not None else self.ttl
        
        self.client.set(
            key,
            json.dumps(value),
            ex=ttl,
        )
        
    def get(self, key: str):
        data = self.client.get(key)
        
        if data is None:
            return None
        
        return json.loads(data)
    
    def delete(self, key: str):
        self.client.delete(key)
        
    def clear(self):
        self.client.flushdb()