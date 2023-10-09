#!/usr/bin/python3

def add_integer(a, b=98):
    """function to add 2 integer

    Args:
        a (int): first value
        b (int, optional): second value. Defaults to 98.

    Raises:
        TypeError: if a is not an int
        TypeError: if b is not an int

    Returns:
        int: sum a + b
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
