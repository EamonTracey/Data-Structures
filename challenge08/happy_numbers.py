#!/usr/bin/env python3

'''
Title:      happy_numbers.py
Abstract:   Determine if a number is a happy number or not using memoization.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       11/14/2022
Questions:

    1. How is seen used in is_happy()?

        The seen hash table stores numbers that the cycle has
        already visited, indicating an infinite cycle which means
        the original number is unhappy.

    2. How is table used in is_happy() to implement memoization?

        The table hash table implements memoization by storing boolean
        values corresponding to the happiness of integers in the cycle.

    3. How many happy numbers are there between 1 and 100 (inclusive)?

        20
'''

from table import Map

import sys

# Functions


def is_happy(n, seen, table):
    ''' Return whether or not n is a happy number.

    >>> is_happy(19, Map(), Map())
    True

    >>> is_happy(2, Map(), Map())
    False

    >>> is_happy(68, Map(), Map())
    True

    >>> is_happy(75, Map(), Map())
    False

    >>> is_happy(91, Map(), Map())
    True
    '''
    if n == 1:
        return True
    if seen.lookup(n):
        return False

    seen.insert(n, 1)

    if not table.lookup(n):
        mut = sum(d ** 2 for d in map(int, str(n)))
        table.insert(n, is_happy(mut, seen, table))

    return table.lookup(n)

# Main Execution


def main(stream=sys.stdin):
    ''' For each number in standard input, determine if it is a happy number,
    and print it out.

    >>> import io
    >>> main(io.StringIO('19\\n2\\n68\\n75\\n91\\n'))
    Is 19 Happy?: Yes
    Is 2 Happy?: No
    Is 68 Happy?: Yes
    Is 75 Happy?: No
    Is 91 Happy?: Yes
    '''
    for line in stream:
        n = int(line.strip())
        happy = is_happy(n, Map(), Map())
        print(f"Is {n} Happy?:", "Yes" if happy else "No")


if __name__ == '__main__':
    main()
