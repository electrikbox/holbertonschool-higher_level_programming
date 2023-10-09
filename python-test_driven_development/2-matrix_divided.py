#!/usr/bin/python3

"""

This module defines a matrix division function.

"""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (list): list of int or float list
        div (int, float): divisor

    Raises:
        TypeError: if matrix is not a list, or empty list
        TypeError: if matrix contains non-int or non-float elements
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not an int or float.
        ZeroDivisionError: if div is 0.

    Returns:
        list: list of int or float divided by divisor
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (
        not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)
    ):
        raise TypeError(error_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
