#AI generated for explorative purposes
"""
from functools import cache, lru_cache
import torch


# Basic Implementation
def gradient_descent(X: torch.Tensor, y: torch.Tensor, lr= float, iters= int) -> torch.Tensor:
    theta = torch.zeros(X.shape[1], requires_grad=True)
    for _ in range(iters):
        loss = ((X.mm(theta.unsqueeze(1)).squeeze() - y) ** 2).mean()
        loss.backward()
        with torch.no_grad():
            theta -= lr * theta.grad
            theta.grad.zero_()
    return theta

# Using functools.cache (Python 3.9+)
@cache
def gradient_descent_cached(X: torch.Tensor, y: torch.Tensor, lr= float, iters= int) -> torch.Tensor:
    theta = torch.zeros(X.shape[1], requires_grad=True)
    for _ in range(iters):
        loss = ((X.mm(theta.unsqueeze(1)).squeeze() - y) ** 2).mean()
        loss.backward()
        with torch.no_grad():
            theta -= lr * theta.grad
            theta.grad.zero_()
    return theta

# Using functools.lru_cache
@lru_cache(maxsize=None)
def gradient_descent_lru(X: torch.Tensor, y: torch.Tensor, lr= float, iters= int) -> torch.Tensor:
    theta = torch.zeros(X.shape[1], requires_grad=True)
    for _ in range(iters):
        loss = ((X.mm(theta.unsqueeze(1)).squeeze() - y) ** 2).mean()
        loss.backward()
        with torch.no_grad():
            theta -= lr * theta.grad
            theta.grad.zero_()
    return theta

'''
# Example usage
X = torch.rand(100, 10)
y = torch.rand(100)

print(gradient_descent(X, y, lr=0.01, iters=1000))
print(gradient_descent_cached(X, y, lr=0.01, iters=1000))
print(gradient_descent_lru(X, y, lr=0.01, iters=1000))
'''

"""