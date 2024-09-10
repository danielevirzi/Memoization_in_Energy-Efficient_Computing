#AI generated for explorative purposes

def is_subset_sum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n-1] > sum:
        return is_subset_sum(arr, n-1, sum)
    return is_subset_sum(arr, n-1, sum) or is_subset_sum(arr, n-1, sum-arr[n-1])

arr = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(arr)
if is_subset_sum(arr, n, sum):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
