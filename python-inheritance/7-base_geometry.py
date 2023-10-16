#!/usr/bin/python3
"""
class that return a raise Exception
"""


class BaseGeometry:
    """
    class that return a raise Exception
    """
    def area(self):
        """
        give area

        Raises:
            Exception: if function is not implemented
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
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than 0")

