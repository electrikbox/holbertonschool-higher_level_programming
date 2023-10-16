#!/usr/bin/python3
"""check if obj is instance of class"""


def is_kind_of_class(obj, a_class):
    """check if obj is instance of class

    Args:
        obj (any): object t check
        a_class (any): given class

    Returns:
        bool: True if is instance, False if not
    """
    return isinstance(obj, a_class)
