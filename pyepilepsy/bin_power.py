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
    band = [0.5,4,7,12,30,70,180]
    power = np.array([0,0,0,0,0,0])
    for freq_index in [0,1,2,3,4,5]:
        freq = float(band[freq_index])
        next_freq = float(band[freq_index + 1])
        power[freq_index] = sum(
            c[int(np.floor(freq / Fs * len(sig))): 
                int(np.floor(next_freq / Fs * len(sig)))]
        )
    return power
