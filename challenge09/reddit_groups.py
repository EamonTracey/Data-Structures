#!/usr/bin/env python3

'''
Title:      reddit_groups.py
Abstract:   Determine how many isolated groups are in graph.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       11/30/2022
Questions:

    1. Does it make a difference if you used BFS or DFS for walk_graph?
    Explain.

        It does NOT make a difference whether you use BFS or DFS for
        walk graph. Either traversal will visit all nodes in the
        group, just possibly in a different order, but order is
        irrelevant for this problem.

    2. What is the average time complexity of walk_graph?

        O(V + E)

        V = # of vertices
        E = # of edges

    3. What is the average time complexity of find_groups?

        O(V^2 + VE)

        V = # of vertices
        E = # of edges
'''

import io
import sys

# Functions


def read_graph(stream=sys.stdin):
    ''' Read one graph from the stream.

    >>> read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    {1: [2, 4], 2: [1, 3], 3: [2], 4: [1]}

    >>> read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    {1: [2], 2: [1], 3: [4], 4: [3]}
    '''
    # if not (n_vertices := stream.readline()):
    #     return {}
    if not (n_vertices := stream.readline()):
        return {}

    n_vertices = int(n_vertices)
    n_edges = int(stream.readline())

    graph = {v: [] for v in range(1, n_vertices + 1)}

    for _ in range(n_edges):
        v1, v2 = map(int, stream.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    return graph


def walk_graph(graph, origin):
    ''' Perform traversal of graph from origin.

    >>> g = read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    >>> walk_graph(g, 1)
    {1, 2, 3, 4}

    >>> g = read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    >>> walk_graph(g, 1)
    {1, 2}
    '''
    frontier = [origin]
    visited = set()

    while frontier:
        vertex = frontier.pop()

        if vertex in visited:
            continue

        visited.add(vertex)

        for neighbor in graph[vertex]:
            frontier.append(neighbor)

    return visited


def find_groups(graph):
    ''' Find isolated groups in graph.

    >>> g = read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    >>> find_groups(g)
    [[1, 2, 3, 4]]

    >>> g = read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    >>> find_groups(g)
    [[1, 2], [3, 4]]
    '''
    groups = []

    for vertex in graph:
        group = walk_graph(graph, vertex)

        if group not in groups:
            groups.append(group)

    return list(map(list, groups))

# Main Execution


def main(stream=sys.stdin):
    ''' For each graph, find the number of isolated graphs, and print them out
    in sorted order.

    >>> main(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n4\\n2\\n1 2\\n3 4\\n10\\n8\\n1 2\\n6 8\\n8 1\\n10 6\\n7 7\\n7 5\\n3 6\\n6 2\\n'))
    Graph 1:
    1 2 3 4
    Graph 2:
    1 2
    3 4
    Graph 3:
    1 2 3 6 8 10
    4
    5 7
    9
    '''
    i = 0
    while graph := read_graph(stream):
        i += 1

        groups = find_groups(graph)

        print(f"Graph {i}:")
        print("\n".join(" ".join(str(v) for v in sorted(group)) for group in groups))


if __name__ == '__main__':
    main()
