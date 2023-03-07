#!/usr/bin/env python3

'''
Title:      tree.py
Abstract:   Implement a binary tree read and walk functions.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   25 minutes
Date:       11/01/2022
Questions:

    1. What is the worst-case time complexity of tree_read()?

        O(n)

    2. What is the worst-case time complexity of tree_walk()?

        O(n)

    3. In tree_walk(), how did you modify BFS to print all the nodes on one
    comma separated line?

        I modified BFS by appending both the left and right children of a given
        node if either of the children is not None. That way, the traversal
        passes through all the None values of a level containing non-None nodes.

    4. In tree_walk(), how did you remove any trailing invalid nodes from your
    output?

        I removed trailing nodes by only appending children nodes if at least
        one child was not None.
'''

from dataclasses import dataclass
from collections import deque

# Classes


@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None

# Functions


def tree_read(array, index=0):
    ''' Return a node-based tree from the given array of values in BFS format.

    >>> tree_read([1, 2, 3])
    Node(value=1, left=Node(value=2, left=None, right=None), right=Node(value=3, left=None, right=None))

    >>> tree_read([1, 2, 3, 4, 0, 0, 6])
    Node(value=1, left=Node(value=2, left=Node(value=4, left=None, right=None), right=None), right=Node(value=3, left=None, right=Node(value=6, left=None, right=None)))
    '''
    if index >= len(array) or not array[index]:
        return None

    # Divide and Conquer and Combine
    return Node(
        array[index],
        tree_read(array, index=2 * index + 1),
        tree_read(array, index=2 * index + 2)
    )


def tree_walk(root):
    ''' Print out the tree in level-by-level order with each level on the same
    line.

    >>> tree_walk(tree_read([1, 2, 3]))
    1, 2, 3
    >>> tree_walk(tree_read([1, 2, 3, 4, 0, 0, 6]))
    1, 2, 3, 4, 0, 0, 6
    '''
    values = []

    queue = deque([root])
    while queue:
        node = queue.popleft()

        if node is None:
            values.append(0)
            continue

        values.append(node.value)
        if node.left is not None or  node.right is not None:
            queue.append(node.left)
            queue.append(node.right)

    print(", ".join(str(val) for val in values))
