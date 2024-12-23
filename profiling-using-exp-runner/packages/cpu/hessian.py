#AI generated for explorative purposes

from functools import cache, lru_cache, wraps
import numpy as np
from time import perf_counter

def timer(func, *args, **kwargs):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        print(f'Starting {func.__name__} at {start}')   # 1
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Finished {func.__name__} at {end}')     # 3
        print(f"Elapsed time: {end - start}")           # 4
        return result                                   # 5                
    return wrapper

@timer
def measure_time(func: callable, *args, **kwargs):
    print(f"Calling {func.__name__} with args: {args}")  # 2
    return func(*args, **kwargs)


# Basic Implementation
def hessian_basic(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    n = x.size
    hessian_matrix = np.zeros((n, n))
    epsilon = np.sqrt(np.finfo(float).eps)
    
    for i in range(n):
        for j in range(n):
            x_ij = x.copy()
            x_ij[i] += epsilon
            x_ij[j] += epsilon
            f_ij = np.sum(x_ij ** 2)
            
            x_i = x.copy()
            x_i[i] += epsilon
            f_i = np.sum(x_i ** 2)
            
            x_j = x.copy()
            x_j[j] += epsilon
            f_j = np.sum(x_j ** 2)
            
            f_0 = np.sum(x ** 2)
            
            hessian_matrix[i, j] = (f_ij - f_i - f_j + f_0) / (epsilon ** 2)
    
    return hessian_matrix

# Using functools.cache (Python 3.9+)
@cache
def hessian_cache(x_tuple: tuple) -> np.ndarray:
    x = np.array(x_tuple)  # Convert tuple back to numpy array
    n = x.size
    hessian_matrix = np.zeros((n, n))
    epsilon = np.sqrt(np.finfo(float).eps)

    for i in range(n):
        for j in range(n):
            x_ij = x.copy()
            x_ij[i] += epsilon
            x_ij[j] += epsilon
            f_ij = np.sum(x_ij ** 2)

            x_i = x.copy()
            x_i[i] += epsilon
            f_i = np.sum(x_i ** 2)

            x_j = x.copy()
            x_j[j] += epsilon
            f_j = np.sum(x_j ** 2)

            f_0 = np.sum(x ** 2)

            hessian_matrix[i, j] = (f_ij - f_i - f_j + f_0) / (epsilon ** 2)

    return hessian_matrix


# Using functools.lru_cache
@lru_cache(maxsize=None)
def hessian_lru_cache(x_tuple: tuple) -> np.ndarray:
    x = np.array(x_tuple)  # Convert tuple back to numpy array
    n = x.size
    hessian_matrix = np.zeros((n, n))
    epsilon = np.sqrt(np.finfo(float).eps)

    for i in range(n):
        for j in range(n):
            x_ij = x.copy()
            x_ij[i] += epsilon
            x_ij[j] += epsilon
            f_ij = np.sum(x_ij ** 2)

            x_i = x.copy()
            x_i[i] += epsilon
            f_i = np.sum(x_i ** 2)

            x_j = x.copy()
            x_j[j] += epsilon
            f_j = np.sum(x_j ** 2)

            f_0 = np.sum(x ** 2)

            hessian_matrix[i, j] = (f_ij - f_i - f_j + f_0) / (epsilon ** 2)

    return hessian_matrix

if __name__ == '__main__':
    # Example usage
    # def high_dim_func(x):
    #     return np.sum(x**2)

    # Example usage:
    x = np.random.rand(100)  # 100-dimensional input
    x_tuple = tuple(x)
    
    print(measure_time(hessian, x))
    
    print(measure_time(hessian_cache, x_tuple))
    print(measure_time(hessian_cache, x_tuple))

    print(measure_time(hessian_lru_cache, x_tuple))
    print(measure_time(hessian_lru_cache, x_tuple))

    assert np.allclose(hessian(x_tuple), hessian_cache(x_tuple)) and np.allclose(hessian_cache(x_tuple), hessian_lru_cache(x_tuple))