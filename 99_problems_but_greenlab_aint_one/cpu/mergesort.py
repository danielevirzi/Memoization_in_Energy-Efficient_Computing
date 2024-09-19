from functools import cache, lru_cache


#### Merge Sort ####

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



def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


@cache
def merge_sort_cache(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_cache(arr[:mid])
    right = merge_sort_cache(arr[mid:])

    return merge(left, right)


@lru_cache
def merge_sort_lru_cache(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_lru_cache(arr[:mid])
    right = merge_sort_lru_cache(arr[mid:])

    return merge(left, right)