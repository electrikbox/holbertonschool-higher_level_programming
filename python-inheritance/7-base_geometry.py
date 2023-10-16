#!/usr/bin/python3
"""
integer validator method
"""


class BaseGeometry:
    """
     a glass to create geometry shape
    """

    def area(self):
        """
        Raises Exception: if function is not implemented
        """

        raise Exception(f"{self.area.__name__}() is not implemented")

    def integer_validator(self, name, value):
        """
        value type validator

        Args:
            name (str): value name
            value (int): value value

        Raises:
            TypeError: if value is not an int
            ValueError: if value is < 0
        """

        if type(value) is not int:
            raise TypeError(name + "must be an integer")

        if value <= 0:
            raise ValueError(name, "must be greater than 0")
