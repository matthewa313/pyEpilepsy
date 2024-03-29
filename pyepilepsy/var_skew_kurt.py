'''
- Sourced from scipy (https://github.com/scipy/scipy)
- Original code by Pierre GF Gerard-Marchant
- Specific optimization from Matthew Anderson
'''

import numpy as np
from .moment import moment

def var_skew_kurt(a, axis=0, bias=False):
    """
    Computes the excess kurtosis of a dataset.
    Kurtosis is the fourth central moment divided by the square of the
    variance minus 3.0.
    If bias is False then the kurtosis is calculated using k statistics to
    eliminate bias coming from biased moment estimators.
    
    Parameters
    ----------
    a : 1-D array
        data for which the kurtosis is calculated
    axis : int or None, optional
        Axis along which the kurtosis is calculated. Default is 0.
        Does not compute for value: none.
    bias : bool, optional
        If False, then the calculations are corrected for statistical bias.
    Returns
    -------
    kurtosis : float64
        The kurtosis of values
    """
    m2 = np.var(a)
    m3 = moment(a, 3)
    m4 = moment(a, 4)
    olderr = np.seterr(all='ignore')
    try:
        skew_vals = vals = np.ma.where(m2 == 0, 0, m3 / m2**1.5)
        kurt_vals = np.ma.where(m2 == 0, 0, m4 / m2**2.0)
    finally:
        np.seterr(**olderr)

    if not bias:
        n = a.count(axis)
        skew_can_correct = (n > 2) & (m2 > 0)
        kurt_can_correct = (n > 3) & (m2 is not ma.masked and m2 > 0)
        if skew_can_correct.any():
            m2 = np.extract(skew_can_correct, m2)
            m3 = np.extract(skew_can_correct, m3)
            nval = np.ma.sqrt((n-1.0)*n)/(n-2.0)*m3/m2**1.5
            np.place(vals, skew_can_correct, nval)
        if kurt_can_correct.any():
            n = np.extract(kurt_can_correct, n)
            m2 = np.extract(kurt_can_correct, m2)
            m4 = np.extract(kurt_can_correct, m4)
            nval = 1.0/(n-2)/(n-3)*((n*n-1.0)*m4/m2**2.0-3*(n-1)**2.0)
            np.place(vals, kurt_can_correct, nval+3.0)
    return m2, skew_vals, kurt_vals-3
