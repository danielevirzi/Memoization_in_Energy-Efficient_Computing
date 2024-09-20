#AI generated for explorative purposes

from functools import lru_cache, cache

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


@cache
def lcs_cache(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_cache(X, Y, m-1, n-1)
    else:
        return max(lcs_cache(X, Y, m, n-1), lcs_cache(X, Y, m-1, n))


@lru_cache(maxsize=None)
def lcs_lru_cache(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_lru_cache(X, Y, m-1, n-1)
    else:
        return max(lcs_lru_cache(X, Y, m, n-1), lcs_lru_cache(X, Y, m-1, n))

# Example usage
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is", lcs(X, Y))
print("Length of LCS using cache is", lcs_cache(X, Y, len(X), len(Y)))
print("Length of LCS using lru_cache is", lcs_lru_cache(X, Y, len(X), len(Y)))
