#!/usr/bin/python3
"""returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """return json representation function
    Args:
        my_obj (any): object to dump
    Returns:
        any: json
    """
    return json.dumps(my_obj)
