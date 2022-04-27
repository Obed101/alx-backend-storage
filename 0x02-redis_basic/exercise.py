#!/usr/bin/env python3
"""
The main class file for the redis implementation
"""
from functools import wraps
from typing import Callable, Optional, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """Counts the number of calls to @method"""
    qualified = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """This's how the Method will work"""
        self._redis.incr(qualified)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """ Returns the history of all calls to Method and return values"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Defines how Method works"""
        _input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", _input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output
    return wrapper


class Cache:
    """ This is the redis caching class """
    def __init__(self) -> None:
        """This is the instance initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores an instance and returns its id"""
        id = str(uuid.uuid4())
        self._redis.set(data, id)
        return id

    def get(self, key: str, fn: Optional[Callable
                                         ] = None) -> Union[str, bytes, int, float]:
        """ This method calls a callable on the @key's value """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        else:
            return value
    
    def get_str(self, key: str) -> str:
        """Gets a string repr of key's value"""
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """Returns key's value converted to int if possible"""
        value = self.get(key)
        try:
            return int(value.decode("utf-8"))
        except ValueError:
            return 0
