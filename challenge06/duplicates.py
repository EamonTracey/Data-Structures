#!/usr/bin/env python3

'''
Title:      duplicates.py
Abstract:   Determine whether or not a line of words contains any duplicates.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questiones:

    1. What is the average time complexity of detect_duplicates()?

        O(n*log(n))

    2. What is the worst-case time complexity of detect_duplicates()?

        O(n*log(n))

    3. What is the worst-case space complexity of detect_duplicates()?

        O(n)

    4. How would you modify the program to make it case in-sensitive?

        To make the program case in-sensitive, I would lowercase
        every word before passing it to the Set.
'''

import sys

from set import Set

# Functions


def detect_duplicates(words):
    ''' Return whether or not the sequence of words contains a duplicate.

    >>> detect_duplicates('a b c'.split())
    False

    >>> detect_duplicates('a b a'.split())
    True

    >>> detect_duplicates('a b c b e f'.split())
    True
    '''
    words_set = Set()
    for word in words:
        if words_set.search(word):
            return True
        else:
            words_set.insert(word)
    return False

# Main Execution


def main(stream=sys.stdin):
    ''' For each line of words, determine if there are any duplicates.

    >>> import io
    >>> main(io.StringIO('a b c\\na b a\\na b c b e f\\n'))
    False
    True
    True
    '''
    for line in stream:
        words = [val for val in line.split()]
        duplicates = detect_duplicates(words)
        print(duplicates)


if __name__ == '__main__':
    main()
