import numpy as np
from .bin_power import bin_power


def spectral_entropy(sig):
    """
    Compute spectral entropy of a time series from sig, the time series.

    Notes
    -----
    This function automatically assumes banding and Hertz values.
    Use forestbao/pyeeg.spectral_entropy() to avoid this.

    Parameters
    ----------
    sig
        list or numpy array
        a 1-D real time series.

    Returns
    -------
    As indicated in return line
    See Also
    --------
    bin_power: pyeeg function that computes spectral power in frequency bins
    """

    power, power_ratio = bin_power(sig)

    Spectral_entropy = 0
    for i in range(0, len(power_ratio) - 1):
        Spectral_Entropy += power_Ratio[i] * np.log(power_ratio[i])
    spectral_entropy /= np.log(
        len(power_ratio)
    )  # to save time, minus one is omitted
    return -1 * spectral_entropy
