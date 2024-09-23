#AI generated for explorative purposes

from functools import cache, lru_cache
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy

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
#@measure_energy(domains=[RaplPackageDomain(0)])
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
@cache
def merge_sort_cache(arr_tuple: tuple) -> list:
    arr = list(arr_tuple)  # Convert tuple back to list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_cache(tuple(arr[:mid]))
    right = merge_sort_cache(tuple(arr[mid:]))

    return merge(left, right)

# Using functools.lru_cache
#@measure_energy(domains=[RaplPackageDomain(0)])
@lru_cache(maxsize=None)
def merge_sort_lru_cache(arr_tuple: tuple) -> list:
    arr = list(arr_tuple)  # Convert tuple back to list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_lru_cache(tuple(arr[:mid]))
    right = merge_sort_lru_cache(tuple(arr[mid:]))

    return merge(left, right)


if __name__ == '__main__':
    # Example usage
    arr = [12, 11, 13, 5, 6, 7]

    print("Normal Merge Sort:", merge_sort(arr))

    arr_tuple = tuple(arr)  # Convert list to tuple for caching
    print("Cache Merge Sort:", merge_sort_cache(arr_tuple))
    print("LRU Cache Merge Sort:", merge_sort_lru_cache(arr_tuple))
