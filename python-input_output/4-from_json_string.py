#!/usr/bin/python3
"""function that returns an object represented by a JSON string"""

import json

def from_json_string(my_str):
    """function that returns an object represented by a JSON string
    Args:
        my_str (str): string to load
    """
    json.loads(my_str)
