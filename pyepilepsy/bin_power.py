import numpy as np

def bin_power(sig):
    """
    This is NOT a general purpose function. Compute power
    in each frequency bin specified by Band from FFT result of
    sig. By default, sig is a real signal.

    Note
    -----
    This function automatically assumes banding and Hertz values.
    Use the following overloaded function to avoid this.

    Parameters
    -----------
    sig
        numpy array
        1-D signal

    Returns
    -------
    power
        list
        spectral power in each frequency bin.
    """

    c = abs ( np.fft.fft(sig) )
    band = [(1,4), (4,8), (7.5,13), (13,30), (30,44)]
    band_lower = [1,4,7.5,13,30]
    band_upper = [4,8,13,30,44]
    power = np.array([0,0,0,0,0,0])
    for freq_index in [0,1,2,3,4]:
        freq = float(band_lower[freq_index])
        next_freq = float(band_upper[freq_index])
        power[freq_index] = sum(
            c[int(np.floor(freq * 30)): 
                int(np.floor(next_freq * 30))]
        )
    power_ratio = power / sum(power)
    return power, power_ratio
