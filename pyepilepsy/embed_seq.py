import numpy as np

def embed_seq(time_series, tau, embedding_dimension):
    """Build a set of embedding sequences from given time series `time_series`
    with lag `tau` and embedding dimension `embedding_dimension`.
    Let time_series = [x(1), x(2), ... , x(N)], then for each i such that
    1 < i <  N - (embedding_dimension - 1) * tau,
    we build an embedding sequence,
    Y(i) = [x(i), x(i + tau), ... , x(i + (embedding_dimension - 1) * tau)].
    All embedding sequences are placed in a matrix Y.
    Parameters
    ----------
    time_series
        numpy.ndarray
        a 1D time series
    tau
        integer
        the lag or delay when building embedding sequence
    embedding_dimension
        integer
        the embedding dimension
    Returns
    -------
    y
        2-embedding_dimension list
        embedding matrix built
    """
    shape = (
        time_series.size - tau * (embedding_dimension - 1),
        embedding_dimension
    )

    strides = (time_series.itemsize, tau * time_series.itemsize)

    return np.lib.stride_tricks.as_strided(
        time_series,
        shape=shape,
        strides=strides
    )
