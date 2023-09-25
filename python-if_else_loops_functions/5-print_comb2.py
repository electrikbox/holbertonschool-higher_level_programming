#!/usr/bin/python3

separator = ", "

for value in range(0, 100):
    if value == 99:
        separator = "\n"
    print("{:02d}".format(value), end=separator)
