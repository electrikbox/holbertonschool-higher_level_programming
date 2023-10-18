#!/usr/bin/python3
"""function to add attribut if pssible"""


def add_attribute(obj, last, first):
    """add attribut
    Args:
        obj (object): object receiving attribut
        last (str): last name
        first (str): first name
    Raises:
        TypeError: if obj not have dict
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, last, first)
