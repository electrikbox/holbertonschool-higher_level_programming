#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""

from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    file = "add_item.json"
    obj_json = []

    if path.exists(file):
        obj_json = load_from_json_file(file)

    for i in range(1, len(argv)):
        obj_json.append(argv[i])

    save_to_json_file(obj_json, file)
