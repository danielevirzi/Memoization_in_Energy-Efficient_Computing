#AI generated for explorative purposes

from functools import cache, lru_cache


def merge(left: list, right: list) -> list:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Basic Implementation
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Using functools.cache (Python 3.9+)
@cache
def merge_sort_cache(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_cache(arr[:mid])
    right = merge_sort_cache(arr[mid:])

    return merge(left, right)

# Using functools.lru_cache
@lru_cache(maxsize=None)
def merge_sort_lru_cache(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_lru_cache(arr[:mid])
    right = merge_sort_lru_cache(arr[mid:])

    return merge(left, right)

'''
# Example usage
arr = [12, 11, 13, 5, 6, 7]

print(merge_sort(arr))
print(merge_sort_cache(arr))
print(merge_sort_lru_cache(arr))
'''