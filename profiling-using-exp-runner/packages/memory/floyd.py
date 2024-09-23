#AI generated for explorative purposes

from functools import cache, lru_cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy
import numpy as np

# Basic Implementation of Floyd-Warshall Algorithm
#@measure_energy(domains=[RaplPackageDomain(0)])
def floyd_warshall(graph: np.ndarray) -> np.ndarray:
    V = len(graph)
    dist = np.copy(graph)
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
def floyd_warshall_cache(graph: np.ndarray) -> np.ndarray:
    V = len(graph)
    dist = np.copy(graph)
    
    @cache
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
#@measure_energy(domains=[RaplPackageDomain(0)])
def floyd_warshall_lru_cache(graph: np.ndarray) -> np.ndarray:
    V = len(graph)
    dist = np.copy(graph)
    
    @lru_cache(maxsize=None)
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
        [0, 3, INF, INF],
        [2, 0, INF, INF],
        [INF, 7, 0, 1],
        [6, INF, INF, 0]
    ])

    print("Basic Implementation:\n", floyd_warshall(graph))
    print("Using functools.cache:\n", floyd_warshall_cache(graph))
    print("Using functools.lru_cache:\n", floyd_warshall_lru_cache(graph))

