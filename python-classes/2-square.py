#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """ Square class that define a square with is size"""

    def __init__(self, size=0):
        """Instantiate a square with optional size

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is under 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
