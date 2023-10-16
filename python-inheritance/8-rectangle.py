#!/usr/bin/python3
"""Create Geometric objects"""


class BaseGeometry:
    """class to implements geometrical shapes"""

    def area(self):
        """Raises an exception when you call this function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Checks a integer value
        Args:
            name (str): The name of the value.
            value (int): The value.
        Raises:
            TypeError: If `value` isn't a integer.
            ValueError: If `value` is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class rectangle
    Args:
        BaseGeometry (BaseGeometry): mother class
    """
    def __init__(self, width, height):
        """init a rectangle
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
