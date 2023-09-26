#!/usr/bin/env python3

def remove_char_at(phrase, n):
    sentence = ""
    for i in range(len(phrase)):
        if i != n:
            sentence += phrase[i]
    return sentence
