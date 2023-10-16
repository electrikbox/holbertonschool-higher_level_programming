#!/usr/bin/python3
""" class Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a square
    Args:
        Rectangle (Rectangle): mother class
    """
    def __init__(self, size):
        """init a square
        Args:
            size (int): square side size
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """give square area
        Returns:
            int: square area
        """
        return self.__size ** 2
