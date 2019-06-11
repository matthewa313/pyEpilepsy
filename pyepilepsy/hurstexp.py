import numpy as np

def hurst(sig):
    """
    Compute the Hurst exponent of sig.
    ----------
    sig
        numpy array 
        1-D signal
    Returns
    -------
    H (float)
    """
    n = sig.size # num timesteps
    t = np.arange(1, n + 1)
    y = sig.cumsum() # marginally more efficient than: np.cumsum(sig)
    mean_t = y / t # running mean

    s_t = np.zeros(n)       # this is more efficient than:
    r_t = s_t               # s_t = np.zeros(n)
                            # r_t = np.zeros(n)

    for i in range(n):
        s_t[i] = np.std(sig[:i + 1])
        x_t = y - t * mean_t[i]
        r_t[i] = np.ptp(x_t[:i + 1])

    r_s = r_t / s_t
    r_s = np.log(r_s)[1:]
    n = np.log(t)[1:]
    a = np.column_stack((n, np.ones(n.size)))
    [H, c] = np.linalg.lstsq(a, r_s)[0]
    return H