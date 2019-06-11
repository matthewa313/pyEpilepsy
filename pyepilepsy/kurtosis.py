'''
- Sourced from scipy (https://github.com/scipy/scipy)
- Original code by Pierre GF Gerard-Marchant
- Specific optimization from Matthew Anderson
'''

import numpy as np
from .moment import moment

def kurtosis(a, axis=0, fisher=True, bias=False):
    """
    Computes the excess kurtosis of a dataset.
    Kurtosis is the fourth central moment divided by the square of the
    variance minus 3.0.
    If bias is False then the kurtosis is calculated using k statistics to
    eliminate bias coming from biased moment estimators.
    
    Parameters
    ----------
    a : ndarray
        data for which the kurtosis is calculated
    axis : int or None, optional
        Axis along which the kurtosis is calculated. Default is 0.
        Does not compute for value: none.
    bias : bool, optional
        If False, then the calculations are corrected for statistical bias.
    Returns
    -------
    kurtosis : array
        The kurtosis of values along an axis.
    """
    m2 = moment(a, 2, axis)
    m4 = moment(a, 4, axis)
    olderr = np.seterr(all='ignore')
    try:
        vals = np.ma.where(m2 == 0, 0, m4 / m2**2.0)
    finally:
        np.seterr(**olderr)

    if not bias:
        n = a.count(axis)
        can_correct = (n > 3) & (m2 is not ma.masked and m2 > 0)
        if can_correct.any():
            n = np.extract(can_correct, n)
            m2 = np.extract(can_correct, m2)
            m4 = np.extract(can_correct, m4)
            nval = 1.0/(n-2)/(n-3)*((n*n-1.0)*m4/m2**2.0-3*(n-1)**2.0)
            np.place(vals, can_correct, nval+3.0)
    return vals - 3
