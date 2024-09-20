#AI generated for explorative purposes

from functools import cache, lru_cache


# Basic Implementation
def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    
# Using functools.cache (Python 3.9+)
@cache
def reverse_string_cache(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string_cache(s[1:]) + s[0]
    
# Using functools.lru_cache
@lru_cache(maxsize=None)
def reverse_string_lru_cache(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string_lru_cache(s[1:]) + s[0]
    
    
'''
# Example usage
word = "greenlab"

print(reverse_string(word))
print(reverse_string_cache(word))
print(reverse_string_lru_cache(word))
'''
