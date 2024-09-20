#AI generated for explorative purposes

from functools import cache, lru_cache

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@cache
def gcd_cache(a, b):
    while b:
        a, b = b, a % b
    return a

@lru_cache(maxsize=None)
def gcd_lru_cache(a, b):
    while b:
        a, b = b, a % b
    return a

"""
# Example calls
print(gcd(48, 18))           # Normal function call
print(gcd_cache(48, 18))     # Function call with @cache decorator
print(gcd_lru_cache(48, 18)) # Function call with @lru_cache decorator
"""