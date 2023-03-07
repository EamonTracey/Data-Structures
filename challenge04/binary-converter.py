# Title: binary-converter.py
# Abstract: This program converts a decimal number into binary utilizing a stack.
# Author: Eamon Tracey
# Email: etracey@nd.edu
# Estimate: 30 minutes
# Date: 10/10/2022

from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data: int):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self) -> Optional[int]:
        if self.head is None:
            return None

        popped = self.head
        self.head = self.head.next
        return popped.data

    def is_empty(self) -> bool:
        return self.head is None

    def top(self) -> int:
        return self.head.data


def input_int(s: str) -> int:
    n = input(s)

    # Ask for number. If the value entered is not a
    # number, keep prompting until a number is entered.
    while 1:
        try:
            n = int(n)
        except ValueError:
            n = input(s)
        else:
            break
    return n


def print_binary(n: int):
    # Push binary digits to stack.
    n_tmp = n
    binary_stack = Stack()
    while n_tmp:
        quo, rem = divmod(n_tmp, 2)
        binary_stack.push(rem)
        n_tmp = quo

    # Print the binary digits.
    print(n, "=>", end=" ")
    curr = binary_stack.head
    while curr is not None:
        print(binary_stack.pop(), end="")
        curr = curr.next
    print()


def main():
    n = input_int("Enter a number: ")

    # Run program until user enters a 0.
    while n > 0:
        print_binary(n)
        n = input_int("Enter a number: ")


main()

