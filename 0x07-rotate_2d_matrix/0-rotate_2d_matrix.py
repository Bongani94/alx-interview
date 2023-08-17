#!/usr/bin/python3
"""
You can assume the matrix will have 2 dimensions
"""


def rotate_2d_matrix(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = matrix
    m.reverse()
    k = len(m)
    for r in range(k):
        for c in range(r):
            m[r][c], m[c][r] = m[c][r], m[r][c]
