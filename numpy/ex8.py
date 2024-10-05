import numpy as np


def one_hot_encoding(vector):
    mat = np.zeros((vector.size, max(vector) + 1), dtype=int)
    mat[np.arange(vector.size), vector] = 1
    return mat


print(one_hot_encoding(np.array([0, 6, 1, 2])))
