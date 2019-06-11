import numpy as np
from .bin_power import bin_power


def spectral_entropy(sig):
    """
    Compute spectral entropy of a time series from sig, the time series.

    Notes
    -----
    This function automatically assumes banding and Hertz values. Use the
    following overloaded function to avoid this.

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

def spectral_entropy(sig, band, Fs):
    """
    Compute spectral entropy of a time series from sig, the time series.

    Parameters
    ----------
    Band
        list
        boundary frequencies (in Hz) of bins. They can be unequal bins, e.g.
        [0.5,4,7,12,30] which are delta, theta, alpha and beta respectively.
        You can also use range() function of Python to generate equal bins and
        pass the generated list to this function.
        Each element of Band is a physical frequency and shall not exceed the
        Nyquist frequency, i.e., half of sampling frequency.
    sig
        list or numpy array
        a 1-D real time series.
    Fs
        integer (passing a float will slow down tremendously)
        the sampling rate in physical frequency
    Returns
    -------
    As indicated in return line
    See Also
    --------
    bin_power: pyeeg function that computes spectral power in frequency bins
    """

    power, power_Ratio = pyeeg.bin_power(sig, band, Fs)

    spectral_entropy = 0
    for i in range(0, len(power_ratio) - 1):
        spectral_entropy += power_ratio[i] * np.log(power_ratio[i])
    spectral_entropy /= np.log( len(power_ratio) )  # to save time, minus one is omitted
    return -spectral_entropy
