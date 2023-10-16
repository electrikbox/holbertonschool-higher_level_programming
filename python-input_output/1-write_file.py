#!/usr/bin/python3
"""writing in file function"""


def write_file(filename="", text=""):
    """_summary_print in file function"""

    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
