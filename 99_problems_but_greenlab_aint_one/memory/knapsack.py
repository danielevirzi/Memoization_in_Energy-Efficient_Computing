#AI generated for explorative purposes

from functools import cache, lru_cache

# Basic Implementation
def knapsack_basic(weights, values, capacity):
    n = len(weights)
    
    def knapsack_recursive(i, remaining_capacity):
        if i < 0 or remaining_capacity <= 0:
            return 0
        if weights[i] > remaining_capacity:
            return knapsack_recursive(i - 1, remaining_capacity)
        else:
            return max(knapsack_recursive(i - 1, remaining_capacity),
                       values[i] + knapsack_recursive(i - 1, remaining_capacity - weights[i]))
    
    return knapsack_recursive(n - 1, capacity)

# Using functools.cache (Python 3.9+)
def knapsack_cache(weights, values, capacity):
    n = len(weights)
    
    @cache
    def knapsack_recursive(i, remaining_capacity):
        if i < 0 or remaining_capacity <= 0:
            return 0
        if weights[i] > remaining_capacity:
            return knapsack_recursive(i - 1, remaining_capacity)
        else:
            return max(knapsack_recursive(i - 1, remaining_capacity),
                       values[i] + knapsack_recursive(i - 1, remaining_capacity - weights[i]))
    
    return knapsack_recursive(n - 1, capacity)

# Using functools.lru_cache (for Python versions before 3.9)
def knapsack_lru_cache(weights, values, capacity):
    n = len(weights)
    
    @lru_cache(maxsize=None)
    def knapsack_recursive(i, remaining_capacity):
        if i < 0 or remaining_capacity <= 0:
            return 0
        if weights[i] > remaining_capacity:
            return knapsack_recursive(i - 1, remaining_capacity)
        else:
            return max(knapsack_recursive(i - 1, remaining_capacity),
                       values[i] + knapsack_recursive(i - 1, remaining_capacity - weights[i]))
    
    return knapsack_recursive(n - 1, capacity)


"""
# Example usage
weights = [1, 2, 3, 4]
values = [10, 20, 30, 40]
capacity = 5

print("Basic Implementation:", knapsack_basic(weights, values, capacity))  # Output: 50
print("Using functools.cache:", knapsack_cache(weights, values, capacity))  # Output: 50
print("Using functools.lru_cache:", knapsack_lru_cache(weights, values, capacity))  # Output: 50
"""