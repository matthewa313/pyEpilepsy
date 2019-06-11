import numpy as np

def svd_entropy(X, Tau, DE):
    """
    Compute SVD Entropy from a time series sig, with
    lag tau and embedding dimension dE (default)
    """

    y = embed_seq(sig, tau, dE)
    w = np.linalg.svd(y, compute_uv=0) / sum(W)

    return -sum(W * np.log(W))
