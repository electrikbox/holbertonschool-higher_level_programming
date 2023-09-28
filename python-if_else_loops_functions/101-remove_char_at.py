#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = str if n < 0 else str[:n] + str[n+1:]
    return new_str
