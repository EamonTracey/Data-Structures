# Title: insertion-sort-recursive.py
# Abstract: This program sorts a given list of integers using a recrusive insertion sort algorithm.
# Author: Eamon Tracey
# Email: etracey@nd.edu
# Estimate: 30 minutes
# Date: 10/12/2022

import sys


# Sort a list of values through a recursive insertion sort.
def insertion_sort(vals: list, i: int = 1):
    # Base case: index to sort has exceeded the list's last index.
    if i >= len(vals):
        return
    # Set the current value to be inserted.
    curr = vals[i]

    # Iterate through values.
    for j, val in enumerate(vals):
        # Once we find a value greater than our current value, we must insert.
        if val >= curr:
            # Perform a right shift.
            for k in range(i, j, -1):
                vals[k] = vals[k - 1]
            # Insert value into correct position.
            vals[j] = curr
            break

    insertion_sort(vals, i + 1)


def main():
    nums_str = input("Enter a list of integers (separated by space): ")
    nums = nums_str.split()

    if not all(num.isdigit() for num in nums):
        print("ERROR: You must only enter integers.", file=sys.stderr)
        return

    nums = list(map(int, nums))

    print("Original:", nums)
    insertion_sort(nums)
    print("Sorted:", nums)


main()
