#!/usr/bin/env python3
"""
The first class file for the redis implementation
"""
from typing import Any
import redis
import uuid


class Cache():
    """ This is the redis caching class """
    def __init__(self, client: redis.Redis()) -> None:
        """This is the instance initializer"""
        _client = client.flushdb()
    
    def store(self, data: Any) -> Any:
        """Stores an instance and returns its id"""
        id = uuid.uuid4
        redis.set(data, id)
        return id
