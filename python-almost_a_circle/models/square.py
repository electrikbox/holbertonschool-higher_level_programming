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

    # INIT ---------------------------------------------------------------

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

    # STR ----------------------------------------------------------------

    def __str__(self):
        """Returns a string representation of the square.
        Returns:
            str: A string in the format "[Class Name] (id) x/y - size".
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
            )

    # UPDATE -------------------------------------------------------------

    def update(self, *args, **kwargs):
        """Updates attributes of square with either args or keyword args.
        Args:
            *args: Variable-length positional arguments for id, size, x, and y.
            **kwargs: Keyword arguments for id, size, x, and y.
        """
        if args:
            attributs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributs):
                    setattr(self, attributs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # TO DICT ------------------------------------------------------------

    def to_dictionary(self):
        """Returns a dictionary representation of a Square instance.
        Returns:
            dict: A dictionary containing the id, size, x, and y of the square.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
