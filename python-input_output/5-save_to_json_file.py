#!/usr/bin/python3
"""function that writes an Object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """save json in a file
    Args:
        my_obj (any): object to save
        filename (str): file where obj is saved
    Returns:
        int: Number of characters written to the file
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
