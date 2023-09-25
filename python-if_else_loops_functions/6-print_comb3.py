#!/usr/bin/python3

separator = ", "

for loop in range(9):
    for num in range(loop + 1, 10):
        if loop == 8 and num == 9:
            separator = "\n"
        print("{}{}".format(loop, num), end=separator)
