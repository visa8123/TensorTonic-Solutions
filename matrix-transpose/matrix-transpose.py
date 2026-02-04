import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    n,m = A.shape
    A_transpose  = np.zeros((m,n), dtype = A.dtype)
    for i in range(n):
        for j in range(m):
            A_transpose[j,i] = A[i,j]
    return A_transpose
