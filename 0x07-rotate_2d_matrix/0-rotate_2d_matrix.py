#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    # Do not return anything, modify matrix in-place instead

    N = len(matrix)

    for r in range(N):
        for c in range(r):
            matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]

    for r in matrix:
        r.reverse()
