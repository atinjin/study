#!/bin/python3

import math
import os
import random
import re
import sys


def get_count(number_dic, value):
    return number_dic[value] if number_dic.get(value) is not None else 0


def freq_query(query_list):
    inverse_dic = {}
    number_dic = {}
    output = []
    for query in query_list:
        operator = query[0]
        value = query[1]
        count = get_count(number_dic, value)
        if operator == 1:  # Insert x in your data structure.
            number_dic[value] = count + 1
            inverse_dic[count] = max(get_count(inverse_dic, count) - 1, 0)
            inverse_dic[count + 1] = get_count(inverse_dic, count + 1) + 1
        elif operator == 2:  # Delete one occurrence of y from your data structure, if present.
            number_dic[value] = max(count - 1, 0)
            inverse_dic[count] = max(get_count(inverse_dic, count) - 1, 0)
            inverse_dic[count - 1] = get_count(inverse_dic, count - 1) + 1
        elif operator == 3:  # Check if any integer is present whose frequency is exactly value. If yes, print 1 else 0.
            if get_count(inverse_dic, value) > 0:
                output.append(1)
            else:
                output.append(0)
        else:
            Exception()
    return output


if __name__ == '__main__':
    queries = [[1, 5],
               [1, 6],
               [3, 2],
               [1, 10],
               [1, 10],
               [1, 6],
               [2, 5],
               [3, 2]]

    ans = freq_query(queries)

    print('\n'.join(map(str, ans)))
