#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    average = 0
    weight = 0
    for tuple in my_list:
        average += (tuple[0] * tuple[1])
        weight += tuple[1]
    return (average / weight)
