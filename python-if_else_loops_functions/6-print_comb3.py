#!/usr/bin/python3

for loop in range(9):
    for num in range(loop + 1, 10):
        separator = "\n" if loop == 8 and num == 9 else ", "
        print("{}{}".format(loop, num), end=separator)
