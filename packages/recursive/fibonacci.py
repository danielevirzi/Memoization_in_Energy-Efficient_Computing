#AI generated for explorative purposes

from functools import cache, lru_cache
from pyJoules.device.rapl_device import RaplPackageDomain
from pyJoules.energy_meter import measure_energy


# Basic Implementation
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Using functools.cache (Python 3.9+)
@cache
def fibonacci_cache(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

# Using functools.lru_cache
@lru_cache(maxsize=None)
def fibonacci_lru_cache(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)


@measure_energy(domains=[RaplPackageDomain(0)])
def wrapper_fibonacci(n: int) -> int:
    return fibonacci(n)

@measure_energy(domains=[RaplPackageDomain(0)])
def wrapper_fibonacci_cache(n: int) -> int:
    return fibonacci_cache(n)

@measure_energy(domains=[RaplPackageDomain(0)])
def wrapper_fibonacci_lru_cache(n: int) -> int:
    return fibonacci_lru_cache(n)
'''
# Example usage
n = 10

print(fibonacci(n))
print(fibonacci_cache(n))
print(fibonacci_lru_cache(n))
'''





