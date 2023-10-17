#!/usr/bin/python3
"""create object from json file"""

import json


def load_from_json_file(filename):
    """create object
    Args:
        filename (str): file to open
    Returns:
        object: from json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
