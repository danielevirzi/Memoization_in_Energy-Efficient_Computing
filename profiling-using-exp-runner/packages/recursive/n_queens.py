#AI generated for explorative purposes

from functools import cache, lru_cache, wraps
from time import perf_counter

def timer(func, *args, **kwargs):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        print(f'Starting {func.__name__} at {start}')   # 1
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Finished {func.__name__} at {end}')     # 3
        print(f"Elapsed time: {end - start}")           # 4
        return result                                   # 5                
    return wrapper

@timer
def measure_time(func: callable, *args, **kwargs):
    print(f"Calling {func.__name__} with args: {args}")  # 2
    return func(*args, **kwargs)


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
def solve_n_queens(board_tuple: tuple, col: int) -> bool:
    board = list(map(list, board_tuple))  # Convert tuple back to list
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1 
            if solve_n_queens(tuple(map(tuple, board)), col + 1):
                return True
            board[i][col] = 0
    return False

# Using functools.cache (Python 3.9+)
@cache
def solve_n_queens_cache(board_tuple: tuple, col: int) -> bool:
    board = list(map(list, board_tuple))  # Convert tuple back to list
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
    board = list(map(list, board_tuple))  # Convert tuple back to list
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
    # initialize the board
    board = [[0 for _ in range(25)] for _ in range(25)]    
    board_tuple = tuple(map(tuple, board))

    print(measure_time(solve_n_queens, board_tuple, 0))
    
    print(measure_time(solve_n_queens_cache, board_tuple, 0))
    
    print(measure_time(solve_n_queens_lru_cache, board_tuple, 0))

    assert solve_n_queens(board_tuple, 0) == solve_n_queens_cache(board_tuple, 0) == solve_n_queens_lru_cache(board_tuple, 0) == True
    
