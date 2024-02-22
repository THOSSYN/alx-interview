#!/usr/bin/python3
"""Inplace matrix rotation"""


def rotate_2d_matrix(matrix) -> None:
    """Rotates a matrix clockwise in place"""
    if not matrix or len(matrix) == 1:
        return

    n = len(matrix)

    # Transpose the matrix in place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row in place
    for row in matrix:
        row.reverse()
