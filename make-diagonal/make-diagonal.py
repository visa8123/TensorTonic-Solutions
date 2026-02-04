import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    #v = np.array(v)
    #n = v.shape[0]
    #diagonal_matrix = np.zeros((n,n),dtype= v.dtype)
    #for i in range(n):
        #diagonal_matrix[i,i] = v[i]
    #return diagonal_matrix
    return np.diag(v)
    


