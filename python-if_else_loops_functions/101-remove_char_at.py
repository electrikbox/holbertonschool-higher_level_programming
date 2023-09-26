#!/usr/bin/env python3
def remove_char_at(str, n):
    sentence = ""
    for i in str:
        if str.index(i) != n:
            sentence += i
    return sentence
