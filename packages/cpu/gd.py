#AI generated for explorative purposes

from functools import cache, lru_cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy
import numpy as np


# Basic Implementation
def hessian(f: callable, x: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    n = x.size
    hessian_matrix = np.zeros((n, n))
    epsilon = np.sqrt(np.finfo(float).eps)
    
    for i in range(n):
        for j in range(n):
            x_ij = x.copy()
            x_ij[i] += epsilon
            x_ij[j] += epsilon
            f_ij = f(x_ij)
            
            x_i = x.copy()
            x_i[i] += epsilon
            f_i = f(x_i)
            
            x_j = x.copy()
            x_j[j] += epsilon
            f_j = f(x_j)
            
            f_0 = f(x)
            
            hessian_matrix[i, j] = (f_ij - f_i - f_j + f_0) / (epsilon ** 2)
    
    return hessian_matrix

# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
@cache
def hessian_cache(f: callable, x: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    n = x.size
    hessian_matrix = np.zeros((n, n))
    epsilon = np.sqrt(np.finfo(float).eps)
    
    for i in range(n):
        for j in range(n):
            x_ij = x.copy()
            x_ij[i] += epsilon
            x_ij[j] += epsilon
            f_ij = f(x_ij)
            
            x_i = x.copy()
            x_i[i] += epsilon
            f_i = f(x_i)
            
            x_j = x.copy()
            x_j[j] += epsilon
            f_j = f(x_j)
            
            f_0 = f(x)
            
            hessian_matrix[i, j] = (f_ij - f_i - f_j + f_0) / (epsilon ** 2)
    
    return hessian_matrix

# Using functools.lru_cache
#@measure_energy(domains=[RaplPackageDomain(0)])
@lru_cache(maxsize=None)
def hessian_lru_cache(f: callable, x: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    n = x.size
    hessian_matrix = np.zeros((n, n))
    epsilon = np.sqrt(np.finfo(float).eps)
    
    for i in range(n):
        for j in range(n):
            x_ij = x.copy()
            x_ij[i] += epsilon
            x_ij[j] += epsilon
            f_ij = f(x_ij)
            
            x_i = x.copy()
            x_i[i] += epsilon
            f_i = f(x_i)
            
            x_j = x.copy()
            x_j[j] += epsilon
            f_j = f(x_j)
            
            f_0 = f(x)
            
            hessian_matrix[i, j] = (f_ij - f_i - f_j + f_0) / (epsilon ** 2)
    
    return hessian_matrix


'''
# Example usage
def high_dim_func(x):
    return np.sum(x**2)

# Example usage:
x = np.random.rand(100)  # 100-dimensional input

print(hessian(high_dim_func, x))
print(hessian_cache(high_dim_func, x))
print(hessian_lru_cache(high_dim_func, x))
'''
