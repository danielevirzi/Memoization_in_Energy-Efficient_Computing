#AI generated for explorative purposes

from functools import cache, lru_cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy
import numpy as np


# Basic Implementation
#@measure_energy(domains=[RaplPackageDomain(0)])
def DFT(x: np.ndarray) -> np.ndarray:
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
@cache
def DFT_cache(x_tuple: tuple) -> np.ndarray:
    x = np.array(x_tuple)  # Convert tuple back to array
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Using functools.lru_cache
#@measure_energy(domains=[RaplPackageDomain(0)])
@lru_cache(maxsize=None)
def DFT_lru_cache(x_tuple: tuple) -> np.ndarray:
    x = np.array(x_tuple)  # Convert tuple back to array
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


if __name__ == '__main__':
    # Example usage
    X = np.random.random(1024)

    print(DFT(X))

    # Convert array to tuple for caching
    X_tuple = tuple(X)

    print(DFT_cache(X_tuple))
    print(DFT_lru_cache(X_tuple))


