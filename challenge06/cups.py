#!/usr/bin/env python3

'''
Title:      cups.py
Abstract:   Determine the minimum amount of time require to fill all cups of water.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questiones:

    1. What is the worst-case time complexity of fill_cups()?

        O(n*log(n))

    2. What is the worst-case space complexity of fill_cups()?

        O(1)

    3. Why is this considered a greedy approach?

        The approach is considered greedy because it attempts
        to perform the most optimal move at each individual
        step. It always attempts to empty the 2 different
        types of cup with the most cups left until only one
        type of cup remains.
'''

import sys

from priority_queue import PriorityQueue

# Functions


def fill_cups(cups):
    ''' Return minimum number of seconds required to fill all cups of water.

    Use a greedy algorithm by attempting to fill two types of cups at a time
    until there is only one remaining type.
    >>> fill_cups([1, 4, 2])
    4

    >>> fill_cups([5, 4, 4])
    7

    >>> fill_cups([5, 0, 0])
    5
    '''
    pq = PriorityQueue(cups)

    seconds = 0
    while 1:
        # Acquire the 2 largest values remaining.
        first = pq.pop()
        second = pq.pop()

        # If the largest value is 0, we are done.
        if first == 0:
            break

        # Otherwise, we must use another second.
        seconds += 1

        # If the second largest value is 0, we can only fill 1 more cup.
        if second == 0:
            pq.push(first - 1)
            pq.push(second)
        # Otherwise, we can fill 2 more cups at once.
        else:
            pq.push(first - 1)
            pq.push(second - 1)

    return seconds


# Main Execution


def main(stream=sys.stdin):
    ''' For each line of cups, determine the minimum number of seconds required
    to fill all cups of water.

    >>> import io
    >>> main(io.StringIO('1 4 2\\n5 4 4\\n5 0 0\\n'))
    4
    7
    5
    '''
    for line in stream:
        cups = [int(val) for val in line.split()]
        seconds = fill_cups(cups)
        print(seconds)


if __name__ == '__main__':
    main()
