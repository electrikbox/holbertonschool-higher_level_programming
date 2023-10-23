#!/usr/bin/python3
"""
represent a base class that will help for future
rectangle and square classes
"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialisation
        Args:
            id (int, optional): object identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
