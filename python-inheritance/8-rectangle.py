#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
