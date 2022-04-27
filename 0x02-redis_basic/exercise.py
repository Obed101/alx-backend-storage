#!/usr/bin/env python3
"""
The main class file for the redis implementation
"""
from typing import Any, Union
import redis
import uuid


class Cache:
    """ This is the redis caching class """
    def __init__(self) -> None:
        """This is the instance initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores an instance and returns its id"""
        id = str(uuid.uuid4())
        redis.set(data, id)
        return id
