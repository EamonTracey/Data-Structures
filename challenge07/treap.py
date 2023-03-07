#!/usr/bin/env python3

'''
Title:      treap.py
Abstract:   Implement a Map class using a treap.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   2.5 hours
Date:       11/07/2022
Questions:

    1. What is worst-case time complexity of Map.insert()?

        O(n)

    2. What is worst-case time complexity of Map.search()?

        O(n)

    3. What role does a Node's priority play during insertion?

        A Node's priority is used to meet the binary heap constraints
        of the treap during insertion. If the left child has a higher priority,
        then the subtree is rotated to the right. If the right child has a
        higher priority, then the subtree is rotated to the left.

    4. How did you use a dictionary in Map._dump_tree() to help you print each
    level on a single line?

        In Map._dump_tree, I implemented a variation of breadth first search in
        which I entered keys into a dictionary corresponding to the keys'
        respective levels. The dictionary stores key-value pairs where the
        key represents the level of the tree and the values are lists
        storing the keys contained by the tree.
'''

from collections import deque, defaultdict
from dataclasses import dataclass
from random import random

# Classes


@dataclass
class Node:
    ''' Node with string key, int value, float priority, and left and right children. '''
    key: str
    value: int = 0
    priority: float = 0
    left: "Node" = None
    right: "Node" = None


class Map:
    ''' Map Implementation based on a treap. '''

    def __init__(self):
        ''' Initialize empty Map.

        >>> m = Map(); not m.root
        True
        '''
        self.root = None

    def insert(self, key, value, priority=None):
        ''' Insert key, value pair into Map.  If key is already in Map, then
        update value.

        >>> m = Map()
        >>> m.insert('D', 0, 60); m.root
        Node(key='D', value=0, priority=60, left=None, right=None)

        >>> m.insert('F', 1, 76); m.root.key        # Rotate Left
        'F'

        >>> m.insert('H', 2, 14); m.root.right.key
        'H'

        >>> m.insert('C', 3, 70); m.root.left.key   # Rotate Right
        'C'

        >>> m.insert('A', 4, 55); m.root.left.left.key
        'A'
        '''
        self.root = self._insert(self.root, key, value, priority)

    def _insert(self, node, key, value, priority=None):
        ''' Recursively insert key, value pair into Map. '''
        # Base case: Invalid node
        if node is None:
            return Node(key, value, priority or random())

        # Base case: Update existing Node
        if key == node.key:
            node.value = value
            return node

        # Recursive: BST invariants
        if key < node.key:
            node.left = self._insert(node.left, key, value, priority)

            # Max-Bin-Heap invariant
            if node.left.priority > node.priority:
                node = Map._rotate_right(node)
        else:
            node.right = self._insert(node.right, key, value, priority)

            # Max-Bin-Heap invariant
            if node.right.priority > node.priority:
                node = Map._rotate_left(node)

        return node

    def lookup(self, key):
        ''' Lookup key in Map and return associated value (None if missing).

        >>> m = Map()
        >>> d = [('sbn', '574'), ('eau', '715'), ('sna', 714), ('nyc', 646)]
        >>> for k, v in d: m.insert(k, v)
        >>> all(m.lookup(k) == v for k, v in d)
        True

        >>> m.lookup('stl')
        '''
        return self._lookup(self.root, key)

    def _lookup(self, node, key):
        ''' Recursively lookup key in Map and return associated value (None if
        missing). '''
        # Base case: Invalid node
        if node is None:
            return None

        # Base case: Matching keys
        if key == node.key:
            return node.value

        if key < node.key:
            return self._lookup(node.left, key)
        else:
            return self._lookup(node.right, key)

    @staticmethod
    def _dump_tree(root):
        ''' Output tree keys in BFS (level-by-level) order.

        - Print out one level per line (with nodes separated by spaces).
        - Do not print any lines with only invalid nodes.

        >>> tree = Node('A', left=Node('B'), right=Node('C'))
        >>> Map._dump_tree(tree)
        A
        B C

        >>> tree = Node('A', left=Node('B', left=Node('C'), right=Node('D')), right=Node('E'))
        >>> Map._dump_tree(tree)
        A
        B E
        C D 0 0

        >>> tree = Node('A', left=Node('B'), right=Node('C', left=Node('D'), right=Node('E')))
        >>> Map._dump_tree(tree)
        A
        B C
        0 0 D E
        '''
        queue = deque([root])
        lmap = defaultdict(list)
        level = 0
        count = 0
        lvl = 1

        # Absurdity
        while queue:
            node = queue.popleft()

            if node is None:
                lmap[level].append("0")
            else:
                lmap[level].append(node.key)
                queue.append(node.left)
                queue.append(node.right)

            count += 1
            if count == lvl:
                count = 0
                lvl = 2 * sum(1 for key in lmap[level] if key != "0")
                level += 1

        # Rambunctiousness
        for l in lmap:
            if any(key != "0" for key in lmap[l]):
                print(" ".join(lmap[l]))

    @staticmethod
    def _rotate_right(p):
        ''' Rotate the sub-tree at parent node to the right.

            P               CL
           / \             /  \
          CL CR     =>    GL   P
         /  \                 / \
        GL  GR              GR   CR

        >>> tree = Node('A', left=Node('B'), right=Node('C'))
        >>> Map._dump_tree(Map._rotate_right(tree))
        B
        0 A
        0 C

        >>> tree = Node('A', left=Node('B', left=Node('C'), right=Node('D')), right=Node('E'))
        >>> Map._dump_tree(Map._rotate_right(tree))
        B
        C A
        0 0 D E
        '''
        cl = p.left
        gr = cl.right

        cl.right = p
        p.left = gr

        return cl

    @staticmethod
    def _rotate_left(p):
        ''' Rotate the sub-tree at parent node to the left.

            P               CR
           / \             /  \
          CL CR     =>    P   GR
            /  \         / \
           GL  GR       CL  GL

        >>> tree = Node('A', left=Node('B'), right=Node('C'))
        >>> Map._dump_tree(Map._rotate_left(tree))
        C
        A 0
        B 0

        >>> tree = Node('A', left=Node('B'), right=Node('C', left=Node('D'), right=Node('E')))
        >>> Map._dump_tree(Map._rotate_left(tree))
        C
        A E
        B D 0 0
        '''
        cr = p.right
        gl = cr.left

        cr.left = p
        p.right = gl

        return cr
