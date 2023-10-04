#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0.0

    score_sum = sum(i * j for i, j in my_list)
    weight_sum = sum(j for i, j in my_list)
    result = score_sum / weight_sum

    return 0 if result == 0 else result
