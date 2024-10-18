#AI generated for explorative purposes

from functools import cache, lru_cache, wraps
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


class UniquePaths:
    
    # Basic Implementation
    def unique_paths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths(m - 1, n) + self.unique_paths(m, n - 1)
    
    # Using functools.cache (Python 3.9+)
    @cache
    def unique_paths_cache(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths_cache(m - 1, n) + self.unique_paths_cache(m, n - 1)
    
    # Using functools.lru_cache
    @lru_cache(maxsize=None)
    def unique_paths_lru_cache(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths_lru_cache(m - 1, n) + self.unique_paths_lru_cache(m, n - 1)
    

if __name__ == '__main__':
    # Example usage
    up = UniquePaths()
    n = 9
    m = 9

    print(measure_time(up.unique_paths, n, m))
    print(measure_time(up.unique_paths_cache, n, m))
    print(measure_time(up.unique_paths_lru_cache, n, m))
    
    assert up.unique_paths(n, m) == up.unique_paths_cache(n, m) == up.unique_paths_lru_cache(n, m)


