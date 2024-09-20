#AI generated for explorative purposes

from functools import lru_cache, cache
import numpy as np

# Basic Implementation
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


"""
# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernel = np.array([[1, 0], [0, -1]])

print("Basic Implementation:\n", convolve2d(matrix, kernel))
print("Using functools.cache:\n", convolve2d_cache(matrix, kernel))
print("Using functools.lru_cache:\n", convolve2d_lru_cache(matrix, kernel))
"""