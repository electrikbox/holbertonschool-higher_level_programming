#!/usr/bin/python3

def islower(c):
    ascii_value = ord(c)
    return 97 <= ascii_value <= 122


def uppercase(str):
    sentence = ""
    for char in str:
        if islower(char):
            sentence += chr(ord(char) - 32)
        else:
            sentence += char

    print("{:s}".format(sentence))
