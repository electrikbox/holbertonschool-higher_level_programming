#!/usr/bin/python3

"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """initializes the rectangle.

        Args:
            width (int, optional): rectangle width. Defaults to 0.
            height (int, optional): rectangle height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter.

        Args:
            value (int): width value.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter.

        Args:
            value (int): height value.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return rectangle_str[:-1]

    def __repr__(self):
        """print representation of a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
