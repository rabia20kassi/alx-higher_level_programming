#!/usr/bin/python3
def uppercase(str):
    for c in str:
        k = ord(c)
        print("{}".format((k >= 97 and k <= 122) and chr(k - 32) or c), end='')
    print()
