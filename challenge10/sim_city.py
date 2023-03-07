#!/usr/bin/env python3

'''
Title:      sim_city.py
Abstract:   Compute the minimum spanning tree of points in a city map.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       12/7/2022
Questions:

    1. What is the average time complexity of build_graph?

        O(V^2)

        V = # of vertices

    2. What is the average time complexity of compute_mst?

        O(V + Elog(E))

        V = # of vertices
        E = # of edges

    3. What is the average space complexity of compute_mst?

        O(V + E)

        V = # of vertices
        E = # of edges

    4. Does the total cost of the minimum spanning tree change if we use
    different starting vertices for compute_mst?  Experiment and then
    explain.

        The total cost of the minimum spanning tree does NOT change if we use
        different starting vertices for compute_mst. This is because Prim's
        algorithm will always choose the minimum weight path regardless of
        starting point. It is possible that a different starting vertex
        gives a different path of equal weight, but it is guaranteed, for any
        starting vertex, that the weight is a minimum.
'''

import collections
import heapq
import io
import math
import random

import requests
import sys

# Constants

POINTS_URL  = 'https://yld.me/raw/jpIx'
POINTS_TEXT = requests.get(POINTS_URL).text

# Read Points


def read_points(stream=sys.stdin):
    ''' Read points from stream.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 2.0, 4.0)]

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 1.0, 2.0), (3, 2.0, 1.0)]

    >>> read_points(points_stream)
    [(0, 0.0, 1.0), (1, 2.0, 3.0), (2, 4.0, 1.0), (3, 1.0, 2.0), (4, 5.0, 2.0)]
    '''
    n = int(stream.readline())
    points = []

    for i in range(n):
        points.append(
            (i, *map(float, stream.readline().split()))
        )

    return points

# Build Graph


def build_graph(points):
    ''' Build adjacency list from list of points.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 3.1622776601683795}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 2.0}, 2: {0: 3.1622776601683795, 1: 2.0, 2: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 1.0, 3: 1.0}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 1.0, 3: 1.0}, 2: {0: 1.0, 1: 1.0, 2: 0.0, 3: 1.4142135623730951}, 3: {0: 1.0, 1: 1.0, 2: 1.4142135623730951, 3: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 2.8284271247461903, 2: 4.0, 3: 1.4142135623730951, 4: 5.0990195135927845}, 1: {0: 2.8284271247461903, 1: 0.0, 2: 2.8284271247461903, 3: 1.4142135623730951, 4: 3.1622776601683795}, 2: {0: 4.0, 1: 2.8284271247461903, 2: 0.0, 3: 3.1622776601683795, 4: 1.4142135623730951}, 3: {0: 1.4142135623730951, 1: 1.4142135623730951, 2: 3.1622776601683795, 3: 0.0, 4: 4.0}, 4: {0: 5.0990195135927845, 1: 3.1622776601683795, 2: 1.4142135623730951, 3: 4.0, 4: 0.0}})
    '''
    graph = collections.defaultdict(dict)

    for point in points:
        for cmpoint in points:
            graph[point[0]][cmpoint[0]] = math.sqrt((point[1] - cmpoint[1]) ** 2 + (point[2] - cmpoint[2]) ** 2)

    return graph

# Compute MST


def compute_mst(graph, start):
    ''' Compute minimum spanning tree.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 1: 0, 2: 1}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 2: 0, 1: 2, 3: 0}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 3: 0, 1: 3, 2: 1, 4: 2}
    '''
    frontier = [(0, start, start)]
    visited = {}

    while frontier:
        weight, target, source = heapq.heappop(frontier)

        if target in visited:
            continue
        visited[target] = source

        for neighbor, weight in graph[target].items():
            heapq.heappush(frontier, (weight, neighbor, target))

    return visited


# Main Execution


def main(stream=sys.stdin):
    ''' For each set of points, build the graph, compute the MST, and then
    print out the total cost.

    >>> main(io.StringIO(POINTS_TEXT))
    Graph 1: 3.41
    Graph 2: 3.00
    Graph 3: 7.07
    Graph 4: 12.73
    Graph 5: 27.08
    '''
    i = 0
    while graph := build_graph(read_points(stream)):
        i += 1

        distance = sum(graph[source][target] for source, target in compute_mst(graph, min(graph)).items())
        print(f"Graph {i}: {distance:.2f}")


if __name__ == '__main__':
    main()
