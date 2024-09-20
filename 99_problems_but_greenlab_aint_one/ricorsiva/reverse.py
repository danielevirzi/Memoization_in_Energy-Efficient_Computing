#AI generated for explorative purposes

from functools import cache, lru_cache


#### Reverse string ####

def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    

@cache
def reverse_string_cache(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string_cache(s[1:]) + s[0]
    

@lru_cache
def reverse_string_lru_cache(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string_lru_cache(s[1:]) + s[0]
    
