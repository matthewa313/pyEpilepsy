# coding=UTF-8
"""
PyEpilepsy, A Python module to extract EEG features to aid in epilepsy prediction.

Email manderson63@cherrycreekschools.org for more information.

**DATA STRUCTURES**

PyEpilepsy uses standard Python and numpy data structures,
so you need to import numpy before using it.

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

I follow this style guide:
http://www.python.org/dev/peps/pep-0008/
"""

from .hurstexp import hurst
from .permutation_entropy import permutation_entropy
from .skew_kurtosis import skew_kurtosis
from .spectral_entropy import spectral_entropy
from .svd_entropy import svd_entropy
