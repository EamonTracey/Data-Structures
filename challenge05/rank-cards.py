# Title: rank-cards.py
# Abstract: This program sorts names based on their respective hands of playing cards.
# Author: Eamon Tracey
# Email: etracey@nd.edu
# Estimate: 30 minutes
# Date: 10/12/2022

import os
import sys


# Map ranks to corresponding number values.
def rank_num(rank: str) -> int:
    rank_map = {"J": 11, "Q": 12, "K": 13}

    if rank.isdigit():
        return int(rank)
    else:
        return rank_map[rank.upper()]


# Map suits to corresponding number values.
def suit_num(suit: str) -> int:
    suit_map = {"S": 3, "H": 2, "D": 1, "C": 0}

    return suit_map[suit.upper()]


def main():
    filepath = input("Enter filepath: ")

    if not os.path.isfile(filepath):
        print("ERROR: Filepath", filepath, "does not exist.", file=sys.stderr)
        return

    hands = dict()
    with open(filepath, "r") as f:
        n = int(f.readline().strip())
        for _ in range(n):
            name, rank, suit = f.readline().strip().split()
            hands[name] = rank_num(rank), suit

    print(hands)

    hands = hands.items()

    print(hands)

    hands_sorted = sorted(hands, key=lambda hand: hand[1], reverse=True)
    print(hands_sorted)
    print(", ".join(hand[0] for hand in hands_sorted))


main()
