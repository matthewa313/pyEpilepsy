from numpy.core import umath
from numpy import float128

def mean(a, axis=1):
    axis = (axis,)
    items = 1
    for ax in axis:
        items *= a.shape[ax]
    rcount = items
    ret = umath.add.reduce(a, axis, float128, None, False)
    return ret / rcount
