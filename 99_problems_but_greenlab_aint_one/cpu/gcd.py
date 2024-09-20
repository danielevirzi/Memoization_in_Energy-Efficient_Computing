#AI generated for explorative purposes

from functools import cache, lru_cache

class GCD:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    @cache
    def gcd_cache(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    @lru_cache(maxsize=None)
    def gcd_lru_cache(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


"""
# Example calls
gcd_instance = GCD()

print(gcd(48, 18))
print(gcd_cache(48, 18))
print(gcd_lru_cache(48, 18))
"""