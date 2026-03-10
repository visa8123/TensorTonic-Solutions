import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X,dtype = float)
    y = np.asarray(y,dtype = float)
    N,D = X.shape
    w = np.zeros(D)
    b = 0.0
    for i in range(steps):
        z = X @ w + b
        p = _sigmoid(z)

        grad_w = (X.T @ (p-y)) / N
        grad_b = np.mean(p-y)

        w = w - (lr*grad_w)
        b = b - (lr*grad_b)
    return w, float(b)
        