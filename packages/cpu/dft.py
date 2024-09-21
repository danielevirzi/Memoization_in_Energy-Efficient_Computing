#AI generated for explorative purposes

from functools import cache, lru_cache
import numpy as np
from pyJoules.device.rapl_device import RaplPackageDomain
from pyJoules.energy_meter import measure_energy


# Basic Implementation
@measure_energy(domains=[RaplPackageDomain(0)])
def DFT(x: np.ndarray) -> np.ndarray:
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Using functools.cache (Python 3.9+)
@cache
@measure_energy(domains=[RaplPackageDomain(0)])
def DFT_cache(x: np.ndarray) -> np.ndarray:
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Using functools.lru_cache
@lru_cache(maxsize=None)
@measure_energy(domains=[RaplPackageDomain(0)])
def DFT_lru_cache(x: np.ndarray) -> np.ndarray:
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

'''
# Example usage
X = np.array([1, 2, 3, 4])

print(DFT(X))
print(DFT_cache(X))
print(DFT_lru_cache(X))
'''

