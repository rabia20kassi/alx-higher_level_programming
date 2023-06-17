#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mulList = a_dictionary.copy()
    for key in mulList:
        mulList[key] *= 2
    return mulList
