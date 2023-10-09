#!/usr/bin/python3
"""

Function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    Args:
        a (int): first value
        b (int, optional): second value. Defaults to 98.
    Returns:
        sum (int) a + b
    """

    a_int = int(a)
    b_int = int(b)

    if not isinstance(a_int, int):
        raise TypeError('a must be an integer')

    if not isinstance(b_int, int):
        raise TypeError('b must be an integer')

    return a_int + b_int
