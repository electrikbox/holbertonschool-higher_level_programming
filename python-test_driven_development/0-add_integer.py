#!/usr/bin/python3
"""

Function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    Args:
        a (int or float): First value.
        b (int or float, optional): Second value. Defaults to 98.

    Raises:
        TypeError: If a or b is not an int or float.

    Returns:
        int: The addition of a and b.
    """

    # if not isinstance(a, (int, float)):
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')

    # if not isinstance(b, (int, float)):
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
