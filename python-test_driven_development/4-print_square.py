#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """print square

    Args:
        size (int): size of square

    Raises:
        TypeError: if size is not a integer or size is a float
        ValueError: if size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    [print("#" * size) for _ in range(size)]
