#AI generated for explorative purposes

from functools import cache, lru_cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy
from time import perf_counter
from functools import wraps

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


if __name__ == '__main__':
    # Example usage
    n = 10

    print(measure_time(fibonacci, n))
    print(measure_time(fibonacci_cache, n))
    print(measure_time(fibonacci_lru_cache, n))




