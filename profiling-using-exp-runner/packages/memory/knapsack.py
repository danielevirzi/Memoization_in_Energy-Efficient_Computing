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
def knapsack_basic(weights_tuple: tuple, values_tuple: tuple, capacity: int) -> int:
    weights = list(weights_tuple)
    values = list(values_tuple)
    n = len(weights)
    
    def knapsack_recursive(i: int, remaining_capacity: int) -> int:
        if i < 0 or remaining_capacity <= 0:
            return 0
        if weights[i] > remaining_capacity:
            return knapsack_recursive(i - 1, remaining_capacity)
        else:
            return max(knapsack_recursive(i - 1, remaining_capacity),
                       values[i] + knapsack_recursive(i - 1, remaining_capacity - weights[i]))
    
    return knapsack_recursive(n - 1, capacity)

# Using functools.cache (Python 3.9+)
@cache
def knapsack_cache(weights_tuple: tuple, values_tuple: tuple, capacity: int) -> int:
    weights = list(weights_tuple)
    values = list(values_tuple)
    n = len(weights)
    
    @cache
    def knapsack_recursive(i: int, remaining_capacity: int) -> int:
        if i < 0 or remaining_capacity <= 0:
            return 0
        if weights[i] > remaining_capacity:
            return knapsack_recursive(i - 1, remaining_capacity)
        else:
            return max(knapsack_recursive(i - 1, remaining_capacity),
                       values[i] + knapsack_recursive(i - 1, remaining_capacity - weights[i]))
    
    return knapsack_recursive(n - 1, capacity)

# Using functools.lru_cache
@lru_cache(maxsize=None)
def knapsack_lru_cache(weights_tuple: tuple, values_tuple: tuple, capacity: int) -> int:
    weights = list(weights_tuple)
    values = list(values_tuple)
    n = len(weights)
    
    @lru_cache(maxsize=None)
    def knapsack_recursive(i: int, remaining_capacity: int) -> int:
        if i < 0 or remaining_capacity <= 0:
            return 0
        if weights[i] > remaining_capacity:
            return knapsack_recursive(i - 1, remaining_capacity)
        else:
            return max(knapsack_recursive(i - 1, remaining_capacity),
                       values[i] + knapsack_recursive(i - 1, remaining_capacity - weights[i]))
    
    return knapsack_recursive(n - 1, capacity)


if __name__ == '__main__':
    # Example usage
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30]
    capacity = 5
    
    weights_tuple = tuple(weights)
    values_tuple = tuple(values)

    print("Basic Implementation:", knapsack_basic(weights_tuple, values_tuple, capacity))
    print(measure_time(knapsack_basic, weights_tuple, values_tuple, capacity))
    
    print(measure_time(knapsack_cache, weights_tuple, values_tuple, capacity))
    print(measure_time(knapsack_cache, weights_tuple, values_tuple, capacity))

    
    print(measure_time(knapsack_lru_cache, weights_tuple, values_tuple, capacity))
    print(measure_time(knapsack_lru_cache, weights_tuple, values_tuple, capacity))

    assert knapsack_basic(weights_tuple, values_tuple, capacity) == knapsack_cache(weights_tuple, values_tuple, capacity) == knapsack_lru_cache(weights_tuple, values_tuple, capacity)

