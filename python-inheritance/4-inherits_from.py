#!/usr/bin/python3
"""check if obj is subclass of class"""


def inherits_from(obj, a_class):
    """check if obj is subclass of class

    Args:
        obj (any): object t check
        a_class (any): given class

    Returns:
        bool: True if is instance, False if not
    """

    return isinstance(obj, a_class) and not issubclass(a_class, obj.__class__)
