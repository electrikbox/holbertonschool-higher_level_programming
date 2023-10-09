#!/usr/bin/python3
"""

Function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    a (int): first value
    b (int, optional): second value. Defaults to 98.
    Returns: sum a + b
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)


print(add_integer(int('inf'), 10))