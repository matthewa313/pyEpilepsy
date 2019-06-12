def hjorth(sig):
    """ Compute Hjorth mobility and complexity of a time series from either two
    cases below:
        1. X, the time series of type list (default)
        2. D, a first order differential sequence of X (if D is provided,
           recommended to speed up)
    In case 1, D is computed using Numpy's Difference function.
    Notes
    -----
    Computed mobility and complexity together to minimize CPU time.
    
    Parameters
    ----------
    X list a time series

    Returns
    -------
    As indicated in return line
    Hjorth mobility and complexity
    """

    D = np.diff(sig).tolist()

    D.insert(0, sig[0])  # pad the first difference
    D = np.array(D)

    n = len(sig)

    M2 = float(sum(D ** 2)) / n
    TP = sum(np.array(X) ** 2)
    M4 = 0
    for i in range(1, len(sig)):
      M4 += (D[i] - D[i - 1]) ** 2
    M4 = M4 / n

    return TP, # Hjorth Activity
        np.sqrt(M2 / TP), # Hjorth Mobility
        np.sqrt(float(M4) * TP / M2 / M2)  # Complexity
