#AI generated for explorative purposes

from functools import lru_cache, cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy
import numpy as np


# Basic Implementation
#@measure_energy(domains=[RaplPackageDomain(0)])
def convolve2d(matrix: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    m, n = matrix.shape
    km, kn = kernel.shape
    output = np.zeros((m - km + 1, n - kn + 1))
    
    def compute_element(i: int, j: int) -> float:
        return np.sum(matrix[i:i+km, j:j+kn] * kernel)
    
    for i in range(m - km + 1):
        for j in range(n - kn + 1):
            output[i, j] = compute_element(i, j)
    
    return output

# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
def convolve2d_cache(matrix: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    m, n = matrix.shape
    km, kn = kernel.shape
    output = np.zeros((m - km + 1, n - kn + 1))
    
    @cache
    def compute_element(i: int, j: int) -> float:
        return np.sum(matrix[i:i+km, j:j+kn] * kernel)
    
    for i in range(m - km + 1):
        for j in range(n - kn + 1):
            output[i, j] = compute_element(i, j)
    
    return output

# Using functools.lru_cache
#@measure_energy(domains=[RaplPackageDomain(0)])
def convolve2d_lru_cache(matrix: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    m, n = matrix.shape
    km, kn = kernel.shape
    output = np.zeros((m - km + 1, n - kn + 1))
    
    @lru_cache(maxsize=None)
    def compute_element(i: int, j: int) -> float:
        return np.sum(matrix[i:i+km, j:j+kn] * kernel)
    
    for i in range(m - km + 1):
        for j in range(n - kn + 1):
            output[i, j] = compute_element(i, j)
    
    return output


if __name__ == '__main__':
    # Example usage
    matrix = np.random.rand(1080, 1920)
    kernel = np.random.rand(3, 3)

    print("Basic Implementation:\n", convolve2d(matrix, kernel))
    print("Using functools.cache:\n", convolve2d_cache(matrix, kernel))
    print("Using functools.lru_cache:\n", convolve2d_lru_cache(matrix, kernel))
