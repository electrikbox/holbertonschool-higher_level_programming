#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        arg_word = 's' if num_arguments > 1 else ''
        print("{} argument{}:".format(num_arguments, arg_word))

    for i, arg in enumerate(arguments, 1):
        print("{}: {}".format(i, arg))
