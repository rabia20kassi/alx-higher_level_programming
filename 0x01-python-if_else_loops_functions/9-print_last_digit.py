#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= (-1)
        number = number % 10
        print(f"{number}", end='')
        return number
    else:
        print("{}".format(number % 10), end='')
        return number % 10
