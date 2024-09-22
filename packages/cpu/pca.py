#AI generated for explorative purposes

from functools import cache, lru_cache
import numpy as np
#from pyJoules.device.rapl_device import RaplPackageDomain
#from pyJoules.energy_meter import measure_energy

# Basic Implementation
#@measure_energy(domains=[RaplPackageDomain(0)])
def pca(X: np.ndarray, num_components: int) -> np.ndarray:
    X_meaned = X - np.mean(X, axis=0)
    cov_matrix = np.cov(X_meaned, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    sorted_index = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_index]
    sorted_eigenvectors = eigenvectors[:, sorted_index]
    eigenvector_subset = sorted_eigenvectors[:, 0:num_components]
    X_reduced = np.dot(eigenvector_subset.transpose(), X_meaned.transpose()).transpose()
    return X_reduced


# Using functools.cache (Python 3.9+)
#@measure_energy(domains=[RaplPackageDomain(0)])
@cache
def pca_cache(X_tuple: tuple, num_components: int) -> np.ndarray:
    X = np.array(X_tuple)  # Convert tuple back to numpy array
    X_meaned = X - np.mean(X, axis=0)
    cov_matrix = np.cov(X_meaned, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    sorted_index = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_index]
    sorted_eigenvectors = eigenvectors[:, sorted_index]
    eigenvector_subset = sorted_eigenvectors[:, 0:num_components]
    X_reduced = np.dot(eigenvector_subset.transpose(), X_meaned.transpose()).transpose()
    return X_reduced

# Using functools.lru_cache
#@measure_energy(domains=[RaplPackageDomain(0)])
@lru_cache(maxsize=None)
def pca_lru_cache(X_tuple: tuple, num_components: int) -> np.ndarray:
    X = np.array(X_tuple)  # Convert tuple back to numpy array
    X_meaned = X - np.mean(X, axis=0)
    cov_matrix = np.cov(X_meaned, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    sorted_index = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_index]
    sorted_eigenvectors = eigenvectors[:, sorted_index]
    eigenvector_subset = sorted_eigenvectors[:, 0:num_components]
    X_reduced = np.dot(eigenvector_subset.transpose(), X_meaned.transpose()).transpose()
    return X_reduced


if __name__ == '__main__':
    # Example usage
    X = np.random.rand(1000, 100)
    num_components = 10

    # Convert numpy array to tuple for caching
    X_tuple = tuple(map(tuple, X))  # Convert 2D array to tuple of tuples

    print('normal:', pca(X, num_components))
    print('cache:',pca_cache(X_tuple, num_components))
    print('lru_cache:', pca_lru_cache(X_tuple, num_components))
