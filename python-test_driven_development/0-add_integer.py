#!/usr/bin/python3
""" Function that adds 2 integers. """

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

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    
    return int(a) + int(b)
