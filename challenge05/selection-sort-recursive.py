# Title: selection-sort-recursive.py
# Abstract: This program sorts a given list of integers using a recrusive selection sort algorithm.
# Author: Eamon Tracey
# Email: etracey@nd.edu
# Estimate: 30 minutes
# Date: 10/12/2022

import sys


# Sort a list of values through a recursive selection sort.
def selection_sort(vals: list, i: int = 0):
    # Base case: index to sort has exceeded the list's second to last index.
    if i >= len(vals) - 1:
        return

    print(vals)

    min_index = i
    for j, val in enumerate(vals[i:]):
        if val < vals[min_index]:
            min_index = i + j

    vals[i], vals[min_index] = vals[min_index], vals[i]

    selection_sort(vals, i + 1)


def main():
    nums_str = input("Enter a list of integers (separated by space): ")
    nums = nums_str.split()

    if not all(num.isdigit() for num in nums):
        print("ERROR: You must only enter integers.", file=sys.stderr)
        return

    nums = list(map(int, nums))

    print("Original:", nums)
    selection_sort(nums)
    print("Sorted:", nums)


main()
