#!/usr/bin/env python3

'''
Title:      balanced.py
Abstract:   Determine wether or not a binary tree is balanced.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       11/07/2022
Questions:

    1. What is the worst-case time complexity of is_balanced()?

        O(n)

    2. What information does is_balanced() return?

        The is_balanced function returns a boolean and an integer.
        The boolean represents whether the tree starting from the
        root node is balanced, and the integer represents the size
        of said tree.
'''

import sys

# Functions


def is_balanced(array, index=0):
    ''' Determine whether or not a binary tree is balanced.

    A binary tree is balanced if:

    1. Left and right sub-trees are balanced.
    2. Difference between heights of left and right sub-trees is no more than 1.

    >>> is_balanced([5, 3, 6])
    (True, 2)

    >>> is_balanced([5, 3, 6, 4])
    (True, 3)

    >>> is_balanced([5, 3, 0, 4])
    (False, 3)

    >>> is_balanced([5, 3, 4, 0, 1])
    (True, 3)

    >>> is_balanced([5, 3, 4, 0, 1, 0, 0, 0, 0, 2])
    (False, 4)
    '''
    # Base case: node outside the array
    if index >= len(array) or not array[index]:
        return True, 0

    # Divide and Conquer
    _, left_height = is_balanced(array, 2 * index + 1)
    _, right_height = is_balanced(array, 2 * index + 2)

    return abs(left_height - right_height) <= 1, 1 + max(left_height, right_height)

# Main Execution


def main(stream=sys.stdin):
    ''' For each line with a tree given in BFS format, output whether or not it
    is balanced.

    >>> import io
    >>> main(io.StringIO('5 3 6\\n5 3 6 4\\n5 3 0 4\\n'))
    Balanced
    Balanced
    Not Balanced
    '''
    for line in stream:
        tree = [int(val) for val in line.strip().split()]
        print("Balanced" if is_balanced(tree)[0] else "Not Balanced")


if __name__ == '__main__':
    main()
