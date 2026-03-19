import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here
    param = np.array(param, dtype=float)
    grad = np.array(grad, dtype=float)
    m = np.array(m, dtype=float)
    v = np.array(v, dtype=float)
    
    m_t = (beta1 * m) + ((1 - beta1) * grad)
    v_t = (beta2 * v) + ((1-beta2) * (grad**2))
    m_cap = m_t / (1- (beta1)**t)
    v_cap = v_t / (1- (beta2)**t)
    param_t = param - (lr * (m_cap/(np.sqrt(v_cap)+eps)))
    return param_t,m_t,v_t