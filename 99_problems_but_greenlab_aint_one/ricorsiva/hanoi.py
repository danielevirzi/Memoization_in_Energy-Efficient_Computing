#AI generated for explorative purposes

from functools import cache, lru_cache


# Basic Implementation
def tower_of_hanoi(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)
    
# Using functools.cache (Python 3.9+)
@cache
def tower_of_hanoi_cache(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi_cache(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi_cache(n-1, auxiliary, target, source)
    
# Using functools.lru_cache
@lru_cache(maxsize=None)
def tower_of_hanoi_lru_cache(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi_lru_cache(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi_lru_cache(n-1, auxiliary, target, source)
    
'''
# Example usage
n = 3
source = "A"
target = "C"
auxiliary = "B"

tower_of_hanoi(n, source, target, auxiliary)
tower_of_hanoi_cache(n, source, target, auxiliary)
tower_of_hanoi_lru_cache(n, source, target, auxiliary)
'''