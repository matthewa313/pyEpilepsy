import numpy as np

[0.5,4,7,12,30], 256

def bin_power(sig):
    """
    This is NOT a general purpose function.
    Compute power in each frequency bin specified by Band from FFT result of
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
    power_ratio
        list
        spectral power in each frequency bin normalized by total power in ALL
        frequency bins.
    """

    c = abs ( np.fft.fft(sig) )
    power = np.array([0,0,0,0])
    for freq_index in [0,1,2,3]:
        freq = float(band[freq_index])
        next_freq = float(band[freq_index + 1])
        power[freq_index] = sum(
            c[int(np.floor(freq / Fs * len(sig))): 
                int(np.floor(next_freq / Fs * len(sig)))]
        )
    power_ratio = power / sum(power)
    return power, power_ratio

def bin_power(sig, band, Fs):
    """
    This is a general function.
    Compute power in each frequency bin specified by Band from FFT result of
    sig.

    Note
    -----
    A real signal can be synthesized, thus not real.

    Parameters
    -----------
    Band
        list
        boundary frequencies (in Hz) of bins. They can be unequal bins, e.g.
        [0.5,4,7,12,30] which are delta, theta, alpha and beta respectively.
        You can also use range() function of Python to generate equal bins and
        pass the generated list to this function.
        Each element of Band is a physical frequency and should not exceed the
        Nyquist frequency, i.e., half of sampling frequency.
    sig
        list
        1-D signal
    Fs
        integer 
        the sampling rate in physical frequency

    Returns
    -------
    power
        list
        spectral power in each frequency bin.
    power_ratio
        list
        spectral power in each frequency bin normalized by total power in ALL
        frequency bins.
    """

    c = abs ( numpy.fft.fft(sig) )
    power = np.zeros(len(band) - 1)
    for freq_index in range(0, len(band) - 1):
        freq = float(band[freq_index])
        next_freq = float(band[freq_index + 1])
        power[freq_index] = sum(
            c[int(numpy.floor(freq / Fs * len(sig))): 
                int(numpy.floor(next_freq / Fs * len(sig)))]
        )
    power_ratio = power / sum(power)
    return power, power_ratio
