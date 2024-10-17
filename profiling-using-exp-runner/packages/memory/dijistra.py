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
def dijkstra(graph_frozen: frozenset, start: str) -> dict:
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
        'A': {'B': 1, 'C': 4, 'D': 3, 'E': 2, 'F': 3, 'G': 2, 'H': 1, 'I': 2},
        'B': {'A': 1, 'C': 2, 'D': 5, 'E': 3, 'F': 4, 'G': 3, 'H': 2, 'I': 3},
        'C': {'A': 4, 'B': 2, 'D': 1, 'E': 2, 'F': 5, 'G': 4, 'H': 3, 'I': 4},
        'D': {'B': 5, 'C': 1, 'A': 3, 'E': 1, 'F': 2, 'G': 3, 'H': 4, 'I': 5},
        'E': {'F': 3, 'G': 2, 'H': 1, 'A': 2, 'B': 3, 'C': 2, 'D': 1},
        'F': {'E': 3, 'G': 2, 'H': 1, 'I': 4, 'A': 3, 'B': 4, 'C': 5, 'D': 2},
        'G': {'E': 2, 'F': 2, 'H': 1, 'I': 3, 'A': 2, 'B': 3, 'C': 4, 'D': 3},
        'H': {'E': 1, 'F': 1, 'G': 1, 'I': 2, 'A': 1, 'B': 2, 'C': 3, 'D': 4},
        'I': {'J': 1, 'K': 2, 'L': 3, 'M': 4, 'A': 2, 'B': 3, 'C': 4, 'D': 5},
        'J': {'I': 1, 'K': 1, 'L': 2, 'M': 3, 'A': 3, 'B': 4, 'C': 5, 'D': 2},
        'K': {'I': 2, 'J': 1, 'L': 1, 'M': 2, 'A': 4, 'B': 5, 'C': 6, 'D': 3},
        'L': {'I': 3, 'J': 2, 'K': 1, 'M': 1, 'A': 5, 'B': 6, 'C': 7, 'D': 4},
        'M': {'I': 4, 'J': 3, 'K': 2, 'L': 1, 'A': 6, 'B': 7, 'C': 8, 'D': 5},
        
    }
    
    frozenset_graph = dict_to_frozenset(graph)

    print("Basic Dijkstra:", dijkstra(frozenset_graph, 'A'))
    print(measure_time(dijkstra, frozenset_graph, 'A'))

    print(measure_time(dijkstra_cache, frozenset_graph, 'A'))
    print(measure_time(dijkstra_cache, frozenset_graph, 'A'))

    print(measure_time(dijkstra_lru_cache, frozenset_graph, 'A'))
    print(measure_time(dijkstra_lru_cache, frozenset_graph, 'A'))
    
    assert dijkstra(frozenset_graph, 'A') == dijkstra_cache(frozenset_graph, 'A') == dijkstra_lru_cache(frozenset_graph, 'A')

