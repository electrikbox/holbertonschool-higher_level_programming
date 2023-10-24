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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """print representation
        Returns:
            str: square representation
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
            )

    def update(self, *args, **kwargs):
        """update square"""
        if args:
            attributs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributs):
                    setattr(self, attributs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of a Square instance."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
