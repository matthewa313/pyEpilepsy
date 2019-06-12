from numpy.core import umath

def mean(a, axis=1):
    axis = (axis,)
    items = 1
    for ax in axis:
        items *= a.shape[ax]
    rcount = items
    ret = umath.add.reduce(a, axis, dtype, None, False)
    return ret / rcount
