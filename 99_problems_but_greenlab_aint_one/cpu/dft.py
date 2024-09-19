from functools import cache, lru_cache
import numpy as np


#### Discrete Fourier Transform (DFT) ####

def DFT(x: np.ndarray) -> np.ndarray:

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


@cache
def DFT_cache(x: np.ndarray) -> np.ndarray:

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


@lru_cache
def DFT_lru_cache(x: np.ndarray) -> np.ndarray:

    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

