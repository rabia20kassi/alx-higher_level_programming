#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    while 0 <= i < len(my_list):
        print("{:d}".format(my_list[i]))
        i -= 1
