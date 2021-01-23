#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

def count_swaps2(arr):
    n = len(arr)
    swap_count = 0
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count, arr[0], arr[len(arr)-1]


def count_swaps(a):
    swap_count = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap_count += 1
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")
    return swap_count, a[0], a[len(a)-1]


if __name__ == '__main__':
    file = open("./input.txt", "r+")
    n = file.readline()
    a = list(map(int, file.readline().rstrip().split()))
    file.close()

    count, first, last = count_swaps2(a)

    assert count == 5
    assert first == 1
    assert last == 4

    file = open("./input1.txt", "r+")
    n = file.readline()
    a = list(map(int, file.readline().rstrip().split()))
    file.close()

    count, first, last = count_swaps(a)

    assert count == 3
    assert first == 1
    assert last == 6

