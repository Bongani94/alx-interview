#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """ Do not return anything, You can assume the matrix will
    have 2 dimensions and will not be empty.
    """
    matrix.reverse()

    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
