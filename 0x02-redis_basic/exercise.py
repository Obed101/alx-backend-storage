#!/usr/bin/env python3
"""
The main class file for the redis implementation
"""
from typing import Any
import redis
import uuid


class Cache():
    """ This is the redis caching class """
    def __init__(self) -> None:
        """This is the instance initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: str) -> Any:
        """Stores an instance and returns its id"""
        id = uuid.uuid4
        redis.set(data, id)
        return id
