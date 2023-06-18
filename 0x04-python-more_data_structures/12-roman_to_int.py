#!/usr/bin/python3
def roman_to_int(roman_string):
    thisdict = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000}
    prev = 0
    sum = 0

    for char in roman_string:
        if thisdict[char] <= prev:
            sum += thisdict[char]
        else:
            sum += thisdict[char] - prev * 2
        prev = thisdict[char]

    return sum
