#AI generated for explorative purposes

from functools import cache, lru_cache


def is_safe(board: list, row: int, col: int) -> bool:
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


# Basic Implementation
def solve_n_queens(board: list, col: int) -> bool:
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False

# Using functools.cache (Python 3.9+)
@cache
def solve_n_queens_cache(board: list, col: int) -> bool:
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_cache(board, col + 1):
                return True
            board[i][col] = 0
    return False

# Using functools.lru_cache
@lru_cache
def solve_n_queens_lru_cache(board: list, col: int) -> bool:
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_lru_cache(board, col + 1):
                return True
            board[i][col] = 0
    return False

'''
# Example usage
board = [[0 for _ in range(8)] for _ in range(8)]

print(solve_n_queens(board, 0))
print(solve_n_queens_cache(board, 0))
print(solve_n_queens_lru_cache(board, 0))
'''