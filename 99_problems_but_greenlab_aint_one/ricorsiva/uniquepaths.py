from functools import cache, lru_cache
import timeit


#### Unique Paths ####

class UniquePaths:
    
    def unique_paths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths(m - 1, n) + self.unique_paths(m, n - 1)
    
    @cache
    def unique_paths_cache(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths_cache(m - 1, n) + self.unique_paths_cache(m, n - 1)
    
    @lru_cache
    def unique_paths_lru_cache(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths_lru_cache(m - 1, n) + self.unique_paths_lru_cache(m, n - 1)

