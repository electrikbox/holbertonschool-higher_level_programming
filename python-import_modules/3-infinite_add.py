#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    result = 0

    if num_arguments != 0:
        result = sum(int(arg) for arg in arguments)

    print("{}".format(result))
