#!/usr/bin/python3
"""
represent a square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    Args:
        Rectangle (Rectangle): Mother class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize square
        Args:
            size (int): square side size
            x (int, optional): x position. Defaults to 0.
            y (int, optional): y position. Defaults to 0.
            id (any, optional): square id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """print representation
        Returns:
            str: square representation
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size
            )
