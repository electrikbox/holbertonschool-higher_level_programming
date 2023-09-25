#!/usr/bin/python3

def islower(c):
    ascii_value = ord(c)
    return 97 <= ascii_value <= 122


def uppercase(str):
    for char in str:
        if islower(char):
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
