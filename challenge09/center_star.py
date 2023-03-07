#!/usr/bin/env python3

'''
Title:      center_star.py
Abstract:   Determine center of star graph.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       11/30/2022
Questions:

    1. If you did not use a defaultdict to represent the graph, how else could
    you have added the edges to the adjaceny list (describe one alternative
    approach)?

    Instead of using a defaultdict, I could have used a dictionary comprehension
    to assign an empty set to each vertex. Then, I would add corresponding
    adjacent vertices to each set.

    2. What is the average time complexity of find_center?

        O(n)
'''

import io
import sys

from collections import defaultdict

# Functions


def read_graph(stream=sys.stdin):
    ''' Read one graph from the stream.

    >>> read_graph(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n'))
    defaultdict(<class 'list'>, {1: [2], 2: [1, 3, 4], 3: [2], 4: [2]})

    >>> read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n1 4\\n'))
    defaultdict(<class 'list'>, {1: [2, 5, 3, 4], 2: [1], 5: [1], 3: [1], 4: [1]})

    >>> read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n2 4\\n'))
    defaultdict(<class 'list'>, {1: [2, 5, 3], 2: [1, 4], 5: [1], 3: [1], 4: [2]})
    '''
    graph = defaultdict(list)

    if not (n := stream.readline()):
        return graph

    n = int(n)
    for _ in range(n):
        v1, v2 = map(int, stream.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    return graph


def find_center(graph):
    ''' Find center vertex of star graph.

    >>> find_center(read_graph(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n')))
    2

    >>> find_center(read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n1 4\\n')))
    1

    >>> find_center(read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n2 4\\n')))
    '''
    n = len(graph) - 1

    for vertex in graph:
        if len(graph[vertex]) == n:
            return vertex

    return None

# Main Execution


def main(stream=sys.stdin):
    ''' For each graph, determine which vertex is the center of the star graph,
    and print it out.

    >>> main(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n4\\n1 2\\n5 1\\n1 3\\n1 4\\n4\\n1 2\\n5 1\\n1 3\\n2 4\\n'))
    Vertex 2 is the center
    Vertex 1 is the center
    There is no center
    '''
    while graph := read_graph(stream):
        center = find_center(graph)

        if center is None:
            print("There is no center")
        else:
            print("Vertex", center, "is the center")


if __name__ == '__main__':
    main()
