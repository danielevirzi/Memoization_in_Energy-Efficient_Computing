from sys import setrecursionlimit
from functools import wraps, cache, lru_cache, singledispatch
from time import perf_counter
import matplotlib.pyplot as plt
import pandas as pd


#### Memoization Decorators ####

def memoize(f: callable) -> callable:       # This is my memoization approach
    memo = {}
    
    @wraps(f)
    def wrapper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    
    return wrapper


def memoization(f: callable) -> callable:   # This is the memoization approach from the slides
    cache = {}
    
    @wraps(f)
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    
    return memoized_func


#### Functions ####

# (1)

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# (2)

def fibonacci_memo(n: int, memo={}) -> int:
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# (3)

@memoize
def fibonacci_memo_decorator(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_memo_decorator(n-1) + fibonacci_memo_decorator(n-2)

# (4)

@memoization
def fibonacci_memoization(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_memoization(n-1) + fibonacci_memoization(n-2)

# (5)

@cache
def fibonacci_cache(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

# (6)

@lru_cache(maxsize=None)
def fibonacci_lru(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)

# (7)

@singledispatch
def fibonacci_sd(n):
    if n < 2:
        return n
    return fibonacci_sd(n-1) + fibonacci_sd(n-2)

@fibonacci_sd.register(dict)
def _(memo, n):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci_sd(memo, n-1) + fibonacci_sd(memo, n-2)
    return memo[n]


#### Class ####

# (8)

class Memoization:
    def __init__(self):
        self.cache = {}
        
    def fibonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n < 2:
            return n
        self.cache[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return self.cache[n]


#### Main ####

def main():
    
    setrecursionlimit(10000)
    n = 40
    memo = {}
    
    
    # (1) No memoization
    start = perf_counter()
    fibonacci(n)
    end = perf_counter()
    fibonacci_time = end-start
    print(f'fibonacci ran in: {fibonacci_time} sec')
    
    # (2) With manual memoization
    start = perf_counter()
    fibonacci_memo(n)
    end = perf_counter()
    fibonacci_memo_time = end-start
    print(f'fibonacci_memo ran in: {fibonacci_memo_time} sec')
    
    # (3) With memoize decorator
    start = perf_counter()
    fibonacci_memo_decorator(n)
    end = perf_counter()
    fibonacci_memo_decorator_time = end-start
    print(f'fibonacci_memo_decorator ran in: {fibonacci_memo_decorator_time} sec')
    
    # (4) With memoization decorator
    start = perf_counter()
    fibonacci_memoization(n)
    end = perf_counter()
    fibonacci_memoization_time = end-start
    print(f'fibonacci_memoization ran in: {fibonacci_memoization_time} sec')
    
    # (5) With cache decorator
    start = perf_counter()
    fibonacci_cache(n)
    end = perf_counter()
    fibonacci_cache_time = end-start
    print(f'fibonacci_cache ran in: {fibonacci_cache_time} sec')
    
    # (6) With lru_cache decorator
    start = perf_counter()
    fibonacci_lru(n)
    end = perf_counter()
    fibonacci_lru_time = end-start
    print(f'fibonacci_lru ran in: {fibonacci_lru_time} sec')
    
    # (7) With singledispatch
    start = perf_counter()
    fibonacci_sd(memo, n)
    end = perf_counter()
    fibonacci_sd_time = end-start
    print(f'fibonacci_sd ran in: {fibonacci_sd_time} sec')
    
    # (8) With class
    start = perf_counter()
    m = Memoization()
    m.fibonacci(n)
    end = perf_counter()
    fibonacci_class_time = end-start
    print(f'fibonacci_class ran in: {fibonacci_class_time} sec')
    
    # Test
    assert fibonacci(n) == fibonacci_memo(n) == fibonacci_memo_decorator(n) == fibonacci_memoization(n) == fibonacci_cache(n) == fibonacci_lru(n) == fibonacci_sd(memo, n) == m.fibonacci(n)    

    # Visualization
    data = {'Algorithm': ['no memoization', 'manual memoization', 'memoize decorator', 'memoization decorator' , 'cache decorator', 'lru_cache decorator', 'singledispatch' ,  'class approach'],
            'Time': [fibonacci_time, fibonacci_memo_time, fibonacci_memo_decorator_time, fibonacci_memoization_time, fibonacci_cache_time, fibonacci_lru_time, fibonacci_sd_time, fibonacci_class_time]}
    dataframe = pd.DataFrame(data)
    dataframe = dataframe.sort_values(by='Time', ascending=False)
    
    
    plt.figure(figsize=(10,5))
    plt.bar(dataframe['Algorithm'], dataframe['Time'])
    plt.yscale('log')
    plt.ylabel('Time (s)')
    plt.xticks(rotation=45, ha='right')
    plt.title('Fibonacci Algorithms Time Comparison')
    plt.tight_layout()
    plt.show()




if __name__ == '__main__':
    main()
    