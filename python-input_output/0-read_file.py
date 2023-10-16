#!/usr/bin/python3
"""Function that read file"""


def read_file(filename=""):
    """reading file function"""
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
