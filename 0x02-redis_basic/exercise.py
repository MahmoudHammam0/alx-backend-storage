#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ increments the count for that key every time the method is called """
    the_key = method.__qualname__

    @wraps(method)
    def wrapper_func(self, *args, **kwargs):
        """ wraper function for count calls """
        self._redis.incr(the_key)
        return method(self, *args, **kwargs)

    return wrapper_func

def call_history(method: Callable) -> Callable:
    """ add its input parameters to one list in redis """

    @wraps(method)
    def wrapper_func(self, *args, **kwargs):
        """ wrapper function for call history """
        inp = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", inp)
        out = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", out)
        return out

    return wrapper_func


class Cache:
    """ Cache class """
    def __init__(self) -> None:
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, int, float, bytes, None]:
        """ the get method of redis """
        res = self._redis.get(key)
        if fn:
            return fn(res)
        else:
            return res

    def get_str(self, key: str) -> str:
        """ convert res to str """
        value = self.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ convert res to int """
        value = self.get(key)
        return value.decode("utf-8")
