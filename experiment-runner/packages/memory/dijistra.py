#AI generated for explorative purposes

from functools import cache, lru_cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy
import heapq

# Basic Implementation
#@measure_energy(domains=[RaplPackageDomain(0)])
def dijkstra(graph: dict, start: str) -> dict:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
@cache
def dijkstra_cache(graph_frozen: frozenset, start: str) -> dict:
    graph = {k: dict(v) for k, v in graph_frozen}  # Convert frozenset back to dict
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Using functools.lru_cache
#@measure_energy(domains=[RaplPackageDomain(0)])
@lru_cache(maxsize=None)
def dijkstra_lru_cache(graph_frozen: frozenset, start: str) -> dict:
    graph = {k: dict(v) for k, v in graph_frozen}  # Convert frozenset back to dict
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Convert graph dict to frozenset for caching
def dict_to_frozenset(d: dict) -> frozenset:
    return frozenset((k, frozenset(v.items())) for k, v in d.items())

if __name__ == '__main__':
    # Example usage
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    print("Basic Dijkstra:", dijkstra(graph, 'A'))

    graph_frozen = dict_to_frozenset(graph)

    print("Cached Dijkstra:", dijkstra_cache(graph_frozen, 'A'))
    print("LRU Cached Dijkstra:", dijkstra_lru_cache(graph_frozen, 'A'))
