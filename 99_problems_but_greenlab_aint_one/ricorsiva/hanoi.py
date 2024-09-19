from functools import cache, lru_cache


#### Tower of Hanoi ####

def tower_of_hanoi(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)
    
    
@cache
def tower_of_hanoi_cache(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi_cache(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi_cache(n-1, auxiliary, target, source)
    

@lru_cache
def tower_of_hanoi_lru_cache(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi_lru_cache(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi_lru_cache(n-1, auxiliary, target, source)