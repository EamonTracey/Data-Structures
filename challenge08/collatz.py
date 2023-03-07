#!/usr/bin/env python3

'''
Title:      collatz.py
Abstract:   Compute the Collatz cycle length using memoization.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       11/14/2022
Questions:

    1. What is stored in the table passed to cycle_length()?

        The table passed to cycle length stores the cycle length
        values of each integer in the cycle.

    2. How is table used in cycle_length() to implement memoization?

        The table implements memoization by storing the cycle length
        values of all previous numbers starting from 1.

    3. What number between 100 and 1000 (inclusive) has the longest cycle
    length?

        871
'''

from table import Map

import sys

# Functions


def cycle_length(n, table):
    ''' Return the collatz cycle length.

    >>> cycle_length(22, Map())
    16

    >>> cycle_length(58, Map())
    20

    >>> cycle_length(71, Map())
    103

    >>> cycle_length(1337, Map())
    45
    '''
    if n == 1:
        return 1

    if not table.lookup(n):
        table.insert(n, 1 + cycle_length(3 * n + 1 if n % 2 else n // 2, table))

    return table.lookup(n)

# Main Execution


def main(stream=sys.stdin):
    ''' For each number in standard input, compute the cycle length, and print
    it out.

    >>> import io
    >>> main(io.StringIO('22\\n58\\n71\\n1337\\n'))
    Cycle Length of 22: 16
    Cycle Length of 58: 20
    Cycle Length of 71: 103
    Cycle Length of 1337: 45
    '''
    for line in stream:
        n = int(line)
        print(f"Cycle Length of {n}: {cycle_length(n, Map())}")


if __name__ == '__main__':
    main()
