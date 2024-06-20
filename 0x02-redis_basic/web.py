#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker  """
import redis
import requests
from functools import wraps


r = redis.Redis()


def url_access(method):
    """ count url access """

    @wraps(method)
    def wrapper_func(url):
        key = "Cached:" + url
        value = r.get(key)
        if value:
            return value.decode("utf-8")
        count = "count:" + url
        content = method(url)
        r.incr(count)
        r.set(key, content, ex=10)
        r.expire(key, 10)
        return content
    return wrapper_func


@url_access
def get_page(url: str) -> str:
    """ track how many times a particular URL was accessed """
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    print(get_page('http://slowwly.robertomurray.co.uk'))
