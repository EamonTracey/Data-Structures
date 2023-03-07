#!/usr/bin/env python3

'''
Title:      set.py
Abstract:   Implement a set using a linked-based binary tree.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   15 minutes
Date:       10/28/2022
Questions:

    1. While performing a DFS, how do you know if node is valid or not?

        When performing a DFS using a linked list as the tree, you know
        if a node is valid if the node is not None.

    2. What is the worst-case time complexity of Set.search()?

        O(n)

    3. What is the worst-case space complexity of Set.search()?

        O(1)
'''

from dataclasses import dataclass

# Classes


@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None


class Set:
    ''' Simple set using a linked-based binary tree. '''

    def __init__(self, root):
        ''' Initialize internal binary tree. 

        >>> s = Set(Node(4, Node(6, Node(3), Node(7)), Node(6))); s.root
        Node(value=4, left=Node(value=6, left=Node(value=3, left=None, right=None), right=Node(value=7, left=None, right=None)), right=Node(value=6, left=None, right=None))
        '''
        self.root = root

    def search(self, value):
        ''' Return whether or not value is contained within the set.

        Call the recursive method on the tree's root and return the result.
        '''
        return self._search(self.root, value)

    def _search(self, node, value):
        ''' Return whether or not value is contained within the set.

        Walk tree using DFS to find value and return True if found (otherwise
        False).

        >>> s = Set(Node(4, Node(6, Node(3), Node(7)), Node(6)))
        >>> all(s.search(n) for n in [3, 4, 6, 7])
        True
        
        >>> any(s.search(n) for n in [0, 1, 2, 5, 9])
        False
        '''
        if not node:
            return False
        elif value == node.value:
            return True
        else:
            return self._search(node.left, value) or self._search(node.right, value)
