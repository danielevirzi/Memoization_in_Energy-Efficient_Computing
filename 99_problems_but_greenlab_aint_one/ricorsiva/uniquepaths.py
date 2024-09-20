#AI generated for explorative purposes

from functools import cache, lru_cache


#### Unique Paths ####

class UniquePaths:
    
    # Basic Implementation
    def unique_paths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths(m - 1, n) + self.unique_paths(m, n - 1)
    
    # Using functools.cache (Python 3.9+)
    @cache
    def unique_paths_cache(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths_cache(m - 1, n) + self.unique_paths_cache(m, n - 1)
    
    # Using functools.lru_cache
    @lru_cache(maxsize=None)
    def unique_paths_lru_cache(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.unique_paths_lru_cache(m - 1, n) + self.unique_paths_lru_cache(m, n - 1)
    

'''
# Example usage
up = UniquePaths()
n = 3
m = 7

print(up.unique_paths(n, m))
print(up.unique_paths_cache(n, m))
print(up.unique_paths_lru_cache(n, m))
'''

