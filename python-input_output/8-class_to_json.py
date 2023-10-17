#!/usr/bin/python3
"""function that return the object dict"""


def class_to_json(obj):
    """return obj dict
    Args:
        obj (cls): given instance from class
    Returns:
        dict: instance dictionnary
    """
    return obj.__dict__
