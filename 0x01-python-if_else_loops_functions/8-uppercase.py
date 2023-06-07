#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format((ord(c) >= 97 and ord(c) <= 122) and chr(ord(c) - 32) or c), end='')
    print()
