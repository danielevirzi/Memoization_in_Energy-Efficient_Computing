#AI generated for explorative purposes

from functools import cache, lru_cache, wraps
import heapq
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
def dijkstra_basic(graph_frozen: frozenset, start: str) -> dict:
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

# Using functools.cache (Python 3.9+)
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
        'A': {'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 1, 'G': 6, 'H': 2, 'I': 7, 'J': 3},
        'B': {'A': 2, 'C': 6, 'D': 7, 'E': 3, 'F': 8, 'G': 4, 'H': 5, 'I': 1, 'J': 9},
        'C': {'A': 3, 'B': 6, 'D': 2, 'E': 8, 'F': 7, 'G': 3, 'H': 4, 'I': 9, 'J': 5},
        'D': {'A': 4, 'B': 7, 'C': 2, 'E': 6, 'F': 5, 'G': 1, 'H': 8, 'I': 2, 'J': 7},
        'E': {'A': 5, 'B': 3, 'C': 8, 'D': 6, 'F': 4, 'G': 7, 'H': 2, 'I': 5, 'J': 6},
        'F': {'A': 1, 'B': 8, 'C': 7, 'D': 5, 'E': 4, 'G': 2, 'H': 3, 'I': 6, 'J': 4},
        'G': {'A': 6, 'B': 4, 'C': 3, 'D': 1, 'E': 7, 'F': 2, 'H': 5, 'I': 3, 'J': 8},
        'H': {'A': 2, 'B': 5, 'C': 4, 'D': 8, 'E': 2, 'F': 3, 'G': 5, 'I': 1, 'J': 7},
        'I': {'A': 7, 'B': 1, 'C': 9, 'D': 2, 'E': 5, 'F': 6, 'G': 3, 'H': 1, 'J': 2},
        'J': {'A': 3, 'B': 9, 'C': 5, 'D': 7, 'E': 6, 'F': 4, 'G': 8, 'H': 7, 'I': 2}
    }

    frozenset_graph = dict_to_frozenset(graph)

    print("Basic Dijkstra:", dijkstra_basic(frozenset_graph, 'A'))
    print(measure_time(dijkstra_basic, frozenset_graph, 'A'))

    print(measure_time(dijkstra_cache, frozenset_graph, 'A'))
    print(measure_time(dijkstra_cache, frozenset_graph, 'A'))

    print(measure_time(dijkstra_lru_cache, frozenset_graph, 'A'))
    print(measure_time(dijkstra_lru_cache, frozenset_graph, 'A'))
    
    assert dijkstra_basic(frozenset_graph, 'A') == dijkstra_cache(frozenset_graph, 'A') == dijkstra_lru_cache(frozenset_graph, 'A')

