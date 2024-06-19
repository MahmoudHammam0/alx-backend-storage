#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Cache class """
    def __init__(self) -> None:
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

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
