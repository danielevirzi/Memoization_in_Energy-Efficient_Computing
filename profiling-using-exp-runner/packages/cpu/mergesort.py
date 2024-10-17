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

def merge(left: list, right: list) -> list:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Basic Implementation
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Using functools.cache (Python 3.9+)
@cache
def merge_sort_cache(arr_tuple: tuple) -> list:
    arr = list(arr_tuple)  # Convert tuple back to list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_cache(tuple(arr[:mid]))
    right = merge_sort_cache(tuple(arr[mid:]))

    return merge(left, right)

# Using functools.lru_cache
@lru_cache(maxsize=None)
def merge_sort_lru_cache(arr_tuple: tuple) -> list:
    arr = list(arr_tuple)  # Convert tuple back to list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_lru_cache(tuple(arr[:mid]))
    right = merge_sort_lru_cache(tuple(arr[mid:]))

    return merge(left, right)


if __name__ == '__main__':
    # Example usage
    arr = [12, 11, 13, 5, 6, 7]
    arr_tuple = tuple(arr)  # Convert list to tuple for caching


    print(measure_time(merge_sort, arr))

    print(measure_time(merge_sort_cache, arr_tuple))
    print(measure_time(merge_sort_cache, arr_tuple))

    print(measure_time(merge_sort_lru_cache, arr_tuple))
    print(measure_time(merge_sort_lru_cache, arr_tuple))

    assert merge_sort(arr) == merge_sort_cache(arr_tuple) == merge_sort_lru_cache(arr_tuple)

