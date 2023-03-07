#!/usr/bin/env python3

'''
Title:      priority_queue.py
Abstract:   Implement a priority queue using an array-based binary tree.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   45 minutes
Date:       10/28/2022
Questions:

    1. While performing a BFS, how do you know if node is valid or not?

        When performing a BFS using an array as the tree, you know if a
        node is valid if the index of the node is less than the length
        of the tree.

    2. What is the worst-case time complexity of PriorityQueue.pop()?

        O(n)

    3. What is the worst-case space complexity of PriorityQueue.pop()?

        O(1)
'''

from collections import deque

# Classes


class PriorityQueue:
    ''' Simple priority queue using an array-based binary tree. '''

    def __init__(self, tree):
        ''' Initialize internal binary tree.

        >>> pq = PriorityQueue([4, 6, 6, 3, 7]); pq.tree
        [4, 6, 6, 3, 7]
        '''
        self.tree = tree

    def pop(self):
        ''' Return the largest value in priority queue.

        Walk tree using BFS to find largest value, place 0 in its place, and
        then return largest value.

        >>> pq = PriorityQueue([4, 6, 6, 3, 7])
        >>> [pq.pop(), pq.pop(), pq.pop(), pq.pop(), pq.pop()]
        [7, 6, 6, 4, 3]
        >>> pq.tree
        [0, 0, 0, 0, 0]
        '''
        max_index = self.tree[0]

        queue = deque([0])
        while queue:
            index = queue.popleft()

            if self.tree[index] > self.tree[max_index]:
                max_index = index

            left = left_child(index)
            right = right_child(index)

            if left < len(self.tree):
                queue.append(left)
            if right < len(self.tree):
                queue.append(right)

        val = self.tree[max_index]
        self.tree[max_index] = 0
        return val

# Functions


def left_child(index):
    ''' Return index of left child.

    >>> left_child(0)
    1

    >>> left_child(1)
    3
    '''
    return 2 * index + 1


def right_child(index):
    ''' Return index of right child.

    >>> right_child(0)
    2

    >>> right_child(1)
    4
    '''
    return 2 * index + 2


def bfs(root):
    ''' Traverse binary tree in breadth-first order '''
    queue = deque([root])                       # Queue of nodes to visit

    while queue:
        node = queue.popleft()                  # Remove next node to visit
        print(node.value)                       # Visit node

        if node.left:  queue.append(node.left)  # Add left child
        if node.right: queue.append(node.right)  # Add right child
