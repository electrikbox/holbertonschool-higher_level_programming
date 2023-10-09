"""
>>> add_integer(1, 2)
3

>>> add_integer(100, -2)
98

>>> add_integer(1.7, 2.5)
3

>>> add_integer("r", 2)
Traceback (most recent call last):
TypeError: a must be an integer

>>> add_integer(-1, "f")
Traceback (most recent call last):
TypeError: b must be an integer

>>> add_integer(1, 2, 3)
Traceback (most recent call last):
TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given

>>> add_integer(10)
108

>>> add_integer()
Traceback (most recent call last):
TypeError: add_integer() missing 1 required positional argument: 'a'

>>> add_integer(1, float("test"))
Traceback (most recent call last):
ValueError: could not convert string to float: 'test'
"""

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


# result = add_integer(1, float("test"))

# print(result)
