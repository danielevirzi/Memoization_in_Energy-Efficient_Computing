# Importing the packages
from packages import *
import numpy as np
from sys import setrecursionlimit
setrecursionlimit(10000)


#CPU----------------

#is_prime
print(is_prime(132**35))
print(is_prime_cache(132**35))
print(is_prime_lru_cache(132**35))
#mandelbrot()

"""
#merge_sort
arr = np.random.rand(10000)
merge_sort(arr)
merge_sort_cache(arr)
merge_sort_lru_cache(arr)
"""

#GCD
n = 484563564
m = 18354234
gcd(n, m)
gcd_cache(n, m)
gcd_lru_cache(n, m)

"""
#DFT
X = np.array([1, 2, 3, 4])
DFT(X)
DFT_cache(X)
DFT_lru_cache(X)
"""

#memory----------------


matrix = np.array([np.random.rand(20), np.random.rand(20), np.random.rand(20), np.random.rand(20), np.random.rand(20), np.random.rand(20), np.random.rand(20), np.random.rand(20), np.random.rand(20)])
kernel = np.array([[1, 0], [0, -1]])

convolve2d(matrix, kernel)
convolve2d_cache(matrix, kernel)
convolve2d_lru_cache(matrix, kernel)

#ricorsive------------
"""
n = 40
wrapper_fibonacci(n)
wrapper_fibonacci_cache(n)
wrapper_fibonacci_lru_cache(n)



n = 3
source = "A"
target = "C"
auxiliary = "B"
tower_of_hanoi(n, source, target, auxiliary)
tower_of_hanoi_cache(n, source, target, auxiliary)
tower_of_hanoi_lru_cache(n, source, target, auxiliary)


board = [[0 for _ in range(8)] for _ in range(8)]
solve_n_queens(board, 0)
solve_n_queens_cache(board, 0)
solve_n_queens_lru_cache(board, 0)
"""
