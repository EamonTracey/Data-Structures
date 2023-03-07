#!/usr/bin/env python3

'''
Title:      anagrams.py
Abstract:   Determine if two words are anagrams.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       11/07/2022
Questions:

    1. What is the worst-case time complexity for count_letters()?

        O(nlog(n))

    2. What is the worst-case time complexity of is_anagram()?

        O(nlog(n))
'''

from treap import Map

import sys

# Functions


def count_letters(word):
    ''' Counts the occurrences of each letter in word and stores it in a Map
    (case insensitive).

    >>> counts = count_letters('aBbCcC')
    >>> counts.lookup('a')
    1
    >>> counts.lookup('b')
    2
    >>> counts.lookup('c')
    3
    >>> counts.lookup('d')
    '''
    treap = Map()
    for letter in word.lower():
        count = treap.lookup(letter)
        if count is None:
            treap.insert(letter, 1, ord(letter))
        else:
            treap.insert(letter, count + 1, ord(letter))
    return treap


def is_anagram(word_a, word_b):
    ''' Returns whether or not two words are anagrams.

    >>> is_anagram('anna', 'naan')
    True

    >>> is_anagram('banana', 'aNaNaB')
    True

    >>> is_anagram('SiLeNt', 'listen')
    True

    >>> is_anagram('KeK', 'eek')
    False

    >>> is_anagram('Nope', 'Topen')
    False

    >>> is_anagram('taco', 'cat')
    False
    '''
    acounts = count_letters(word_a)
    bcounts = count_letters(word_b)
    return acounts.root == bcounts.root

# Main Execution


def main(stream=sys.stdin):
    ''' For each pair of words on each line, determine if they are anagrams,
    and print out the result.

    >>> import io
    >>> main(io.StringIO('taco cat\\nanna naan\\nSiLeNt listen\\n'))
    taco and cat are not anagrams!
    anna and naan are anagrams!
    SiLeNt and listen are anagrams!
    '''
    for line in stream:
        words = line.split()
        if is_anagram(words[0], words[1]):
            print(words[0], "and", words[1], "are anagrams!")
        else:
            print(words[0], "and", words[1], "are not anagrams!")


if __name__ == '__main__':
    main()
