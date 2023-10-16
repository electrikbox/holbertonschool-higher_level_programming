#!/usr/bin/python3
"""append in file function"""


def append_write(filename="", text=""):
    """append in file function"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
