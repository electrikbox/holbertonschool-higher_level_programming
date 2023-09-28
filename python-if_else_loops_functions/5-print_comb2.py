#!/usr/bin/python3

for value in range(0, 100):
    separator = "\n" if value == 99 else ", "
    print("{:02d}".format(value), end=separator)
