#AI generated for explorative purposes

from functools import cache, lru_cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy
import itertools


# Basic Implementation
#@measure_energy(domains=[RaplPackageDomain(0)])
def generate_permutations(tup: tuple) -> tuple:
    return list(itertools.permutations(tup))

# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
@cache
def generate_permutations_cache(tup: tuple) -> tuple:
    return list(itertools.permutations(tup))

# Using functools.lru_cache
#@measure_energy(domains=[RaplPackageDomain(0)])
@lru_cache(maxsize=None)
def generate_permutations_lru_cache(tup: tuple) -> tuple:
    return list(itertools.permutations(tup))


if __name__ == '__main__':
    # Example Usage
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    print(generate_permutations(tup))
    print(generate_permutations_cache(tup))
    print(generate_permutations_lru_cache(tup))
