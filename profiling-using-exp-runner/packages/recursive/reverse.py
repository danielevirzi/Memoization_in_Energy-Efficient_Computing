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


# Basic Implementation
def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    
# Using functools.cache (Python 3.9+)
@cache
def reverse_string_cache(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string_cache(s[1:]) + s[0]
    
# Using functools.lru_cache
@lru_cache(maxsize=None)
def reverse_string_lru_cache(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string_lru_cache(s[1:]) + s[0]
    
    
if __name__ == '__main__':
    # Example usage
    word = "abcde" * 30

    print(measure_time(reverse_string, word))
    print(measure_time(reverse_string_cache, word))
    print(measure_time(reverse_string_lru_cache, word))
    
    assert reverse_string(word) == reverse_string_cache(word) == reverse_string_lru_cache(word)


