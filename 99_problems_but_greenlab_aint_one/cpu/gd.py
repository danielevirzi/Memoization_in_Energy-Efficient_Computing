#AI generated for explorative purposes

from functools import cache, lru_cache
import torch


#### Gradient Descent ####

def gradient_descent(X: torch.Tensor, y: torch.Tensor, lr= float, iters= int) -> torch.Tensor:
    theta = torch.zeros(X.shape[1], requires_grad=True)
    for _ in range(iters):
        loss = ((X.mm(theta.unsqueeze(1)).squeeze() - y) ** 2).mean()
        loss.backward()
        with torch.no_grad():
            theta -= lr * theta.grad
            theta.grad.zero_()
    return theta

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

@lru_cache
def gradient_descent_lru(X: torch.Tensor, y: torch.Tensor, lr= float, iters= int) -> torch.Tensor:
    theta = torch.zeros(X.shape[1], requires_grad=True)
    for _ in range(iters):
        loss = ((X.mm(theta.unsqueeze(1)).squeeze() - y) ** 2).mean()
        loss.backward()
        with torch.no_grad():
            theta -= lr * theta.grad
            theta.grad.zero_()
    return theta