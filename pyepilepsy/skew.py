import numpy as np
from .moment import moment

def skew(a, axis=0, bias=True):
    """
    Computes the skewness of a data set.
    Parameters
    ----------
    a : ndarray
        data
    axis : int or None, optional
        Axis along which skewness is calculated. Default is 0.
        If None, compute over the whole array `a`.
    bias : bool, optional
        If False, then the calculations are corrected for statistical bias.
    Returns
    -------
    skewness : ndarray
        The skewness of values along an axis, returning 0 where all values are
        equal.
    Notes
    -----
    For more details about `skew`, see `stats.skew`.
    """
    a, axis = _chk_asarray(a,axis)
    n = a.count(axis)
    m2 = moment(a, 2, axis)
    m3 = moment(a, 3, axis)
    olderr = np.seterr(all='ignore')
    try:
        vals = ma.where(m2 == 0, 0, m3 / m2**1.5)
    finally:
        np.seterr(**olderr)

    if not bias:
        can_correct = (n > 2) & (m2 > 0)
        if can_correct.any():
            m2 = np.extract(can_correct, m2)
            m3 = np.extract(can_correct, m3)
            nval = ma.sqrt((n-1.0)*n)/(n-2.0)*m3/m2**1.5
            np.place(vals, can_correct, nval)
    return vals
