#!/usr/bin/python3
alphabet = ""
ascii_a = ord('a')
ascii_z = ord('z')

for ascii_value in range(ascii_a, ascii_z + 1):
    alphabet += chr(ascii_value)

print(f"{alphabet}", end="")
