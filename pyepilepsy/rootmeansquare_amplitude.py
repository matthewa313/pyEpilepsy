import numpy as np

def rms(sig):
    return np.sqrt(np.mean(np.square(sig)))
