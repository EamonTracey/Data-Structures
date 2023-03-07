#!/usr/bin/env python3

'''
Title:      invert.py
Abstract:   Invert binary tree.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   25 minutes
Date:       11/01/2022
Questions:

    1. What is the worst-case time complexity of tree_invert()?

        O(n)

    2. How do you swap two values in Python without a temporary value?

        Python offers the following syntax to swap two values:
            a, b = b, a
'''

import sys

from tree import tree_read, tree_walk

# Functions


def tree_invert(node):
    ''' Invert tree in-place using divide and conquere.

    >>> tree_walk(tree_invert(tree_read([1, 2, 3])))
    1, 3, 2

    >>> tree_walk(tree_invert(tree_read([1, 2, 3, 4, 0, 0, 6])))
    1, 3, 2, 6, 0, 0, 4
    '''
    # Base case
    if node is None:
        return

    # Divide and Conquer!
    node.left, node.right = tree_invert(node.right), tree_invert(node.left)

    return node


# Main Execution


def main(stream=sys.stdin):
    ''' For each line, read in the tree in BFS format, print it, invert it, and
    then print it again.

    >>> import io
    >>> main(io.StringIO('1 2 3\\n1 2 3 4 0 0 6\\n'))
    1, 2, 3
    1, 3, 2
    1, 2, 3, 4, 0, 0, 6
    1, 3, 2, 6, 0, 0, 4
    '''
    for line in stream:
        tree = tree_read([int(val) for val in line.strip().split()])
        tree_walk(tree)
        tree_invert(tree)
        tree_walk(tree)


if __name__ == '__main__':
    main()
