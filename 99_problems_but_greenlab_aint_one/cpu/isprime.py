#AI generated for explorative purposes

from functools import cache, lru_cache

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@cache
def is_prime_cache(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@lru_cache(maxsize=None)
def is_prime_lru_cache(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

"""
# Example calls
print(is_prime(29))           # Normal function call
print(is_prime_cache(29))     # Function call with @cache decorator
print(is_prime_lru_cache(29)) # Function call with @lru_cache decorator
"""