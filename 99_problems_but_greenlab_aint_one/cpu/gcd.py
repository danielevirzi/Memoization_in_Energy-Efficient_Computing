#AI generated for explorative purposes

from functools import cache, lru_cache



class GCD:
    
    # Basic Implementation
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # Using functools.cache (Python 3.9+)
    @cache
    def gcd_cache(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    # Using functools.lru_cache
    @lru_cache(maxsize=None)
    def gcd_lru_cache(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


"""
# Example usage
gcd_instance = GCD()
n = 48
m = 18

print(gcd(n, m))
print(gcd_cache(n, m))
print(gcd_lru_cache(n, m))
"""