#!/usr/bin/python3
"""function that return if instance is part of the class"""


def is_same_class(obj, a_class):
    """check if is instance of class

    Args:
        obj (any): object to check
        a_class (any): given class

    Returns:
        bool: True if instance of class, False if not
    """
    if type(obj) == a_class:
        return True
    return False
