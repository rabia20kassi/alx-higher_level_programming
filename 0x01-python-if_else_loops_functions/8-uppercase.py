#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c >= 'a' and c <= 'z':
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print('')
