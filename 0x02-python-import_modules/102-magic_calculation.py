#!/usr/bin/python3
def magic_calculation(a, b):
    from calculator_1 import add, sub
    if a < b:
        sum = add(a, b)
        for num in range(4, 6):
            sum = add(sum, num)
        return sum
    else:
        return sub(a, b)
