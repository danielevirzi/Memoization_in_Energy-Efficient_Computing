#AI generated for explorative purposes

from functools import cache, lru_cache
from pyJoules.device.rapl_device import RaplPackageDomain
from pyJoules.energy_meter import measure_energy

# Basic Implementation
@measure_energy(domains=[RaplPackageDomain(0)])
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Using functools.cache (Python 3.9+)
@cache
@measure_energy(domains=[RaplPackageDomain(0)])
def gcd_cache(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Using functools.lru_cache
@lru_cache(maxsize=None)
@measure_energy(domains=[RaplPackageDomain(0)])
def gcd_lru_cache(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

"""
# Example usage
n = 48
m = 18

print(gcd(n, m))
print(gcd_cache(n, m))
print(gcd_lru_cache(n, m))
"""