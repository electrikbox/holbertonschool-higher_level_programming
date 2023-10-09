#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """ Square class that define a square with is size"""

    def __init__(self, size=0):
        """Instantiate a square with optional size

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """return square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the square size

        Args:
            value (int): square size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is under 0

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """print square with # in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
