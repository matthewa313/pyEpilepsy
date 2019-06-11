'''
- Sourced from scipy (https://github.com/scipy/scipy)
- Original code by Pierre GF Gerard-Marchant
- Specific optimization from Matthew Anderson
'''

import numpy as np

def moment(a, moment, axis=0):
    """
    Calculates the nth moment about the mean for a sample.
    Parameters
    ----------
    a : 1D numpy array
       data
    moment : int, optional
       order of central moment that is returned
    axis : int or None, optional
       Axis along which the central moment is computed. Default is 0.
       If None, compute over the whole array `a`.
    Returns
    -------
    n-th central moment : ndarray or float
       The appropriate moment along the given axis or over all values if axis
       is None. The denominator for the moment calculation is the number of
       observations, no degrees of freedom correction is done.
    """
    if moment == 1:
        return np.float64(0.0)
    else:
        # Exponentiation by squares: form exponent sequence
        n_list = [moment]
        current_n = moment
        while current_n > 2:
            if current_n % 2:
                current_n = (current_n-1)/2
            else:
                current_n /= 2
            n_list.append(current_n)

        # Starting point for exponentiation by squares
        a_zero_mean = a - np.ma.expand_dims(a.mean(axis), axis)
        if n_list[-1] == 1:
            s = a_zero_mean.copy()
        else:
            s = a_zero_mean**2

        # Perform multiplications
        for n in n_list[-2::-1]:
            s = s**2
            if n % 2:
                s *= a_zero_mean
        return s.mean(axis)
