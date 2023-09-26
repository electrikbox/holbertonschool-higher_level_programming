#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(ord('z'), ord('a') - 1, -1):
        char = chr(i)
        if i % 2 == 1:
            char = char.upper()
        print("{}".format(char), end="")
