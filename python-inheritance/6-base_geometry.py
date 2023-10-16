#!/usr/bin/python3
"""
class that return a raise Exception
"""


class BaseGeometry:
    """
    class that return a raise Exception
    """
    def area(self):
        raise Exception(f"{self.area.__name__}() is not implemented")
