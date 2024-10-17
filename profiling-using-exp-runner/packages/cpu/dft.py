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
def DFT(x_tuple: tuple) -> np.ndarray:
    x = np.array(x_tuple)  # Convert tuple back to array
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Using functools.cache (Python 3.9+)
@cache
def DFT_cache(x_tuple: tuple) -> np.ndarray:
    x = np.array(x_tuple)  # Convert tuple back to array
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Using functools.lru_cache
@lru_cache(maxsize=None)
def DFT_lru_cache(x_tuple: tuple) -> np.ndarray:
    x = np.array(x_tuple)  # Convert tuple back to array
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


if __name__ == '__main__':
    X = np.random.random(1024)
    X_tuple = tuple(X)
    
    print(measure_time(DFT, X_tuple))
    
    print(measure_time(DFT_cache, X_tuple))
    print(measure_time(DFT_cache, X_tuple))

    print(measure_time(DFT_lru_cache, X_tuple))
    print(measure_time(DFT_lru_cache, X_tuple))
    
    assert np.allclose(DFT(X), DFT_cache(X_tuple)) and np.allclose(DFT(X), DFT_lru_cache(X_tuple))



