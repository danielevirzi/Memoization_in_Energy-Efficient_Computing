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

# Basic Implementation of Floyd-Warshall Algorithm
def floyd_warshall(graph_tuple: tuple) -> np.ndarray:
    graph = np.array(graph_tuple)
    V = len(graph)
    dist = np.copy(graph)
    
    def compute_distance(i: int, j: int, k: int) -> int:
        if k == -1:
            return dist[i][j]
        return min(compute_distance(i, j, k-1), compute_distance(i, k, k-1) + compute_distance(k, j, k-1))
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = compute_distance(i, j, k)
    
    return dist

# Using functools.cache (Python 3.9+)
@cache    
def floyd_warshall_cache(graph_tuple: tuple) -> np.ndarray:
    graph = np.array(graph_tuple)
    V = len(graph)
    dist = np.copy(graph)
    
    def compute_distance(i: int, j: int, k: int) -> int:
        if k == -1:
            return dist[i][j]
        return min(compute_distance(i, j, k-1), compute_distance(i, k, k-1) + compute_distance(k, j, k-1))
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = compute_distance(i, j, k)
    
    return dist

# Using functools.lru_cache
@lru_cache(maxsize=None)
def floyd_warshall_lru_cache(graph_tuple: tuple) -> np.ndarray:
    graph = np.array(graph_tuple)
    V = len(graph)
    dist = np.copy(graph)
    
    def compute_distance(i: int, j: int, k: int) -> int:
        if k == -1:
            return dist[i][j]
        return min(compute_distance(i, j, k-1), compute_distance(i, k, k-1) + compute_distance(k, j, k-1))
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = compute_distance(i, j, k)
    
    return dist

if __name__ == '__main__':
    # Example usage
    INF = float('inf')
    graph = np.array([
        [0, 3, INF, INF, 7, 8, 3, 2],
        [3, 0, 4, 2, INF, INF, 1, 5],
        [3, 0, 4, 2, INF, INF, 1, 5],
        [8, 0, 2, 1, INF, INF, 4, 6],
        [2, 0, INF, INF, 4, 0, 2, 3],
        [INF, 7, 0, 1, 2, 6, 0, 4],
        [6, INF, INF, 0, 0, 2, 0, 2],
        [2, 3, 4, 1, 2, 3, 4, 0]
    ])
    
    graph_tuple = tuple(map(tuple, graph))

    print("Basic Implementation:\n", floyd_warshall(graph_tuple))
    print(measure_time(floyd_warshall, graph_tuple))
    
    print(measure_time(floyd_warshall_cache, graph_tuple))
    print(measure_time(floyd_warshall_cache, graph_tuple))

    print(measure_time(floyd_warshall_lru_cache, graph_tuple))
    print(measure_time(floyd_warshall_lru_cache, graph_tuple))

    assert np.allclose(floyd_warshall(graph_tuple), floyd_warshall_cache(graph_tuple)) and np.allclose(floyd_warshall_cache(graph_tuple), floyd_warshall_lru_cache(graph_tuple))


