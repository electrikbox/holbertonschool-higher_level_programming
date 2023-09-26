#!/usr/bin/env python3

def remove_char_at(str, n):
    sentence = ""
    for i in range(len(str)):
        if i != n:
            sentence += str[i]
    return sentence
