#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        min = list(a_dictionary.keys())[0]
        max = a_dictionary[min]
        for i, j in a_dictionary.items():
            if j > max:
                max = j
                min = i
        return min
    else:
        return None
