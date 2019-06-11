# coding=UTF-8

"""
PyEpilepsy, A Python module to extract EEG features to aid in epilepsy prediction.

Email manderson63@cherrycreekschools.org for more information.

**DATA STRUCTURES**

PyEpilepsy only uses standard Python and numpy data structures,
so you need to import numpy before using it.
For numpy, please visit http://numpy.scipy.org

To install numpy from the command line
> pip install numpy (or)
> pip3 install numpy

To install numpy from a python environment:
!pip install numpy (or)
!pip3 install numpy

To import numpy to your python project:
import numpy (or)
import numpy as np

**STYLE CONVENTIONS**

I follow the following style guide for my progra to code my program
http://www.python.org/dev/peps/pep-0008/

--------------------------------------------------

"""

'''from .entropy import ap_entropy, permutation_entropy, samp_entropy, spectral_entropy, svd_entropy
from .spectrum import bin_power
from .detrended_fluctuation_analysis import dfa
from .embedded_sequence import embed_seq
from .fisher_info import fisher_info
from .fractal_dimension import hfd, pfd
from .hjorth_mobility_complexity import hjorth
from .hurst import hurst
from .information_based_similarity import information_based_similarity
from .largest_lyauponov_exponent import LLE
'''

from .hurstexp import hurst
from .spectral_entropy import spectral_entropy
