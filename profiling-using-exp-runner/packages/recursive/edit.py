#AI generated for explorative purposes

from functools import cache, lru_cache, wraps
from time import perf_counter
import sys

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

def random_string(length: int) -> str:
    import random
    import string
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Basic Implementation
def edit_distance(str1: str, str2: str, m: int, n: int) -> int:
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)
    return 1 + min(edit_distance(str1, str2, m, n-1),    
                   edit_distance(str1, str2, m-1, n),    
                   edit_distance(str1, str2, m-1, n-1)) 


# Using functools.cache (Python 3.9+)
@cache
def edit_distance_cache(str1: str, str2: str, m: int, n: int) -> int:
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return edit_distance_cache(str1, str2, m-1, n-1)
    return 1 + min(edit_distance_cache(str1, str2, m, n-1),    
                   edit_distance_cache(str1, str2, m-1, n),    
                   edit_distance_cache(str1, str2, m-1, n-1))  


# Using functools.lru_cache
@lru_cache(maxsize=None)
def edit_distance_lru_cache(str1: str, str2: str, m: int, n: int) -> int:
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return edit_distance_lru_cache(str1, str2, m-1, n-1)
    return 1 + min(edit_distance_lru_cache(str1, str2, m, n-1),    
                   edit_distance_lru_cache(str1, str2, m-1, n),    
                   edit_distance_lru_cache(str1, str2, m-1, n-1))



if __name__ == '__main__':
    # set recursion limit to the maximum
    sys.setrecursionlimit(10**6)
    
    str1 = random_string(7)
    str2 = random_string(7)
    m = len(str1)
    n = len(str2)

    print(measure_time(edit_distance, str1, str2, m, n))
    
    print(measure_time(edit_distance_cache, str1, str2, m, n))
    
    print(measure_time(edit_distance_lru_cache, str1, str2, m, n))
    
    assert edit_distance(str1, str2, m, n) == edit_distance_cache(str1, str2, m, n) == edit_distance_lru_cache(str1, str2, m, n)    
