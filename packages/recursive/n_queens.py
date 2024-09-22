#AI generated for explorative purposes

from functools import cache, lru_cache
import copy
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy


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
def solve_n_queens_cache(board_tuple: tuple, col: int) -> bool:
    board = [list(row) for row in board_tuple]  # Convert tuple back to list
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_cache(tuple(map(tuple, board)), col + 1):
                return True
            board[i][col] = 0
    return False

# Using functools.lru_cache
@lru_cache(maxsize=None)
def solve_n_queens_lru_cache(board_tuple: tuple, col: int) -> bool:
    board = [list(row) for row in board_tuple]  # Convert tuple back to list
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_lru_cache(tuple(map(tuple, board)), col + 1):
                return True
            board[i][col] = 0
    return False


if __name__ == '__main__':
    board = [[0 for _ in range(8)] for _ in range(8)]
    print("Basic Implementation:", solve_n_queens(copy.deepcopy(board), 0))
    board_tuple = tuple(map(tuple, board))
    print("Cache Implementation:", solve_n_queens_cache(board_tuple, 0))
    print("LRU Cache Implementation:", solve_n_queens_lru_cache(board_tuple, 0))
