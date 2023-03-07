# Title: que-with-two-stacks.py
# Abstract: This program implements a queue utilizing two stacks, one as an inbox and the other as an outbox.
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


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enque(self, data: int):
        self.in_stack.push(data)

    def deque(self) -> int:
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def display(self):
        out_reversed = Stack()
        curr = self.out_stack.head
        while curr is not None:
            out_reversed.push(curr.data)
            curr = curr.next

        print("BACK", end=" ")

        # Print the input stack, then the output stack reversed.
        curr = self.in_stack.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        while not out_reversed.is_empty():
            print(out_reversed.pop(), end=" ")

        print("FRONT")


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


def main():
    print(
        "Queue Operations:\n"
        "\t1) Enqueue\n"
        "\t2) Dequeue\n"
        "\t3) Display\n"
    )

    queue = Queue()

    op = input("\nOption: ")
    while 1:
        if op == "1":
            n = input_int("Number to enqueue: ")
            queue.enque(n)
        elif op == "2":
            queue.deque()
        elif op == "3":
            queue.display()
        else:
            break

        op = input("\nOption: ")


main()

