# Title: closest-numbers.py
# Abstract: This program finds all pairs of the closest numbers in a list of numbers.
# Author: Eamon Tracey
# Email: etracey@nd.edu
# Estimate: 30 minutes
# Date: 10/12/2022

import os
import sys


# Return list of pairs of the closest numbers.
def closest_numbers(nums: list) -> list:
    # The list should have at least 2 elements.
    if len(nums) < 2:
        return []

    closest_diff = abs(nums[0] - nums[1])
    closest = [(nums[0], nums[1])]

    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums):
            # Do not consider pairs of the same element (same key).
            if i == j:
                continue

            # Do not consider pairs that have already been found.
            if any({n1, n2} == set(clos) for clos in closest):
                print("found")
                print(closest)
                print(n1, n2)
                continue

            diff = abs(n1 - n2)

            if diff == closest_diff:
                closest.append((n1, n2))
            elif diff < closest_diff:
                closest_diff = diff
                closest.clear()
                closest.append((n1, n2))

    return closest


def main():
    filepath = input("Enter filepath: ")

    if not os.path.isfile(filepath):
        print("ERROR: Filepath", filepath, "does not exist.", file=sys.stderr)
        return

    nums = list()
    with open(filepath, "r") as f:
        f.readline()
        nums = list(map(int, f.readline().strip().split()))

    for pair in closest_numbers(nums):
        print(*pair)


main()
