#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """ Square class that define a square with is size"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a square with optional size

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Square position. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """return square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the square position

        Args:
            value (int tuple): x and y square position

        Raises:
            TypeError: if value is not a tuple
            TypeError: if values in tuple are not int
            TypeError: if int value in tuple are <
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """print square with # in stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for j in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
