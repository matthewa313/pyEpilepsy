import numpy as np
from .embed_seq import embed_seq

def permutation_entropy(sig, n, tau):
    """
    Compute Permutation Entropy of a given time series sig, specified by
    permutation order n and embedding lag tau.
    Parameters
    ----------
    sig
        numpy array
        a time series
    n
        integer
        Permutation order
    tau
        integer
        Embedding lag
    Returns
    ----------
    PE
       float
       permutation entropy
    Notes
    ----------
    Suppose the given time series is X =[x(1),x(2),x(3),...,x(N)].
    We first build embedding matrix Em, of dimension(n*N-n+1),
    such that the ith row of Em is x(i),x(i+1),..x(i+n-1). Hence
    the embedding lag and the embedding dimension are 1 and n
    respectively. We build this matrix from a given time series,
    sig, by calling pyEpilepsy function embed_seq(sig,1,n).
    We then transform each row of the embedding matrix into
    a new sequence, comprising a set of integers in range of 0,..,n-1.
    The order in which the integers are placed within a row is the
    same as those of the original elements:0 is placed where the smallest
    element of the row was and n-1 replaces the largest element of the row.
    To calculate the Permutation entropy, we calculate the entropy of PeSeq.
    In doing so, we count the number of occurrences of each permutation
    in PeSeq and write it in a sequence, RankMat. We then use this sequence to
    calculate entropy by using Shannon's entropy formula.
    Permutation entropy is usually calculated with n in range of 3 and 7.
    References
    ----------
    Bandt, Christoph, and Bernd Pompe. "Permutation entropy: a natural
    complexity measure for time series." Physical Review Letters 88.17
    (2002): 174102.
    """

    pe_seq = []
    em = embed_seq(sig, tau, n)

    for i in range(0, len(em)):
        r = []
        z = []

        for j in range(0, len(em[i])):
            z.append(em[i][j])

        for j in range(0, len(em[i])):
            z.sort()
            r.append(z.index(em[i][j]))
            z[z.index(em[i][j])] = -1

        pe_seq.append(r)

    rank_mat = []

    while len(pe_seq) > 0:
        rank_mat.append(pe_seq.count(pe_seq[0]))
        sig = pe_seq[0]
        for j in range(0, pe_seq.count(pe_seq[0])):
            pe_seq.pop(pe_seq.index(sig))

    rank_mat = np.array(rank_mat)
    rank_mat = np.true_divide(rank_mat, rank_mat.sum())
    entropy_mat = np.multiply(np.log2(rank_mat), rank_mat)

    return -entropy_mat.sum()
