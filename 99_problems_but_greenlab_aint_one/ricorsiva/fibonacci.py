#AI generated for explorative purposes

from functools import cache, lru_cache


#### Fibonacci sequence ####

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def fibonacci_cache(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


@lru_cache
def fibonacci_lru_cache(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)





