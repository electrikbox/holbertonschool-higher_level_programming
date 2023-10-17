#!/usr/bin/python3
import json

"""function that writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """save json in a file
    Args:
        my_obj (any): object to save
        filename (str): file where obj is save
    Returns:
        json: write file
    """

    json_obj = json.dumps(my_obj)
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(json_obj)
