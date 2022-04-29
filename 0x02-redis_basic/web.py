#!/usr/bin/env python3
"""
Obtains the html page or a url
"""
import redis
import requests

_redis = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """This function caches an obtained document from a url"""
    _redis.set(f"cached:{url}", count)
    response = requests.get(url)
    _redis.incr(f"count:{url}")
    _redis.setex(f"cached:{url}", 10, _redis.get(f"cached:{url}"))

    return response.text


if __name__ == "__main__":
    get_page("http://slowly.robertomurray.co.uk")
