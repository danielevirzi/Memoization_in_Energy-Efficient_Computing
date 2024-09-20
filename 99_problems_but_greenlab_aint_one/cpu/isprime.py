#AI generated for explorative purposes

from functools import cache, lru_cache


# Basic Implementation
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Using functools.cache (Python 3.9+)
@cache
def is_prime_cache(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Using functools.lru_cache
@lru_cache(maxsize=None)
def is_prime_lru_cache(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

"""
# Example usage
n = 29

print(is_prime(n))
print(is_prime_cache(n))
print(is_prime_lru_cache(n))
"""