#!/usr/bin/python3
"""
represent a rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """Rectanle class
    Args:
        Base (Base): Mother class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize
        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int, optional): rectangle pos x. Defaults to 0.
            y (int, optional): rectangle pos y. Defaults to 0.
            id (int, optional): geometry id. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """give rectangle area
        Returns:
            int: rectangle area
        """
        return self.width * self.height
