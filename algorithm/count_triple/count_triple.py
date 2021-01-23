#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def count_triplets_better2(arr, r):
    """
    For the one way scanning, we can find the triples at once.
    We are not able to search again for finding the number divided into R.
    That makes time complexity increased.
    To prevent this, memory the previous number and the count.
    Then we can use it getting the existence of the proper previous number and its count.
    In the same way, we could apply the second number and third number.
    """
    count = 0
    first = defaultdict(int)
    second = defaultdict(int)

    for num in arr:
        count += second[num]
        second[num * r] = second[num * r] + first[num]
        first[num * r] = first[num * r] + 1

    return count


def count_triplets_better(arr, r):
    count = 0
    diction = dict()
    dict_pairs = dict()

    for i in reversed(arr):
        if i*r in dict_pairs:
            count += dict_pairs[i*r]
        if i*r in diction:
            dict_pairs[i] = dict_pairs.get(i, 0) + diction[i*r]

        diction[i] = diction.get(i, 0) + 1
    return count


def count_triplets(arr, r):
    """
    This is brute-force algorithm.
    """
    if len(arr) < 3:
        return 0

    result = []
    for i in range(len(arr)):
        first = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == (first * r):
                second = arr[j]
                for k in range(j+1, len(arr)):
                    if arr[k] == (second * r):
                        result.append([i, j, k])
    return len(result)


if __name__ == '__main__':
    file = open("count_triple_test3.txt", "r+")
    nr = file.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, file.readline().rstrip().split()))

    # ans = count_triplets(arr, r)
    ans2 = count_triplets_better2(arr, r)

    # print(str(ans) + '\n')
    print(str(ans2) + '\n')
