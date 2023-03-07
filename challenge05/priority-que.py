# Title: priority-que.py
# Abstract: This program implements a priority queue type that prioritizes dequeing the largest number.
# Author: Eamon Tracey
# Email: etracey@nd.edu
# Estimate: 30 minutes
# Date: 10/12/2022

from typing import Optional


class PriorityQueue:
    def __init__(self):
        self._vals = []

    # Enqueue new element through simple append.
    def enque(self, n: int):
        self._vals.append(n)

    # Deqeueue largest element using a linear search.
    def deque(self) -> Optional[int]:
        if self.is_empty():
            return None

        max_index = 0
        for i, val in enumerate(self._vals):
            if val > self._vals[max_index]:
                max_index = i
        return self._vals.pop(max_index)

    # Check if the queue is empty.
    def is_empty(self) -> bool:
        return len(self._vals) == 0


def main():
    queue = PriorityQueue()

    print(
        "Menu Options:\n"
        "\t1. Enqueue\n"
        "\t2. Dequeue\n"
        "\t3. Check If The Queue Is Empty"
    )

    cont = "y"
    while cont.lower() == "y":
        op = int(input("\nEnter option: "))

        if op == 1:
            new = int(input("Enter number to queue: "))
            queue.enque(new)
        elif op == 2:
            print("Dequeued", queue.deque())
        elif op == 3:
            print("Queue IS empty." if queue.is_empty() else "Queue IS NOT empty.")

        cont = input("Continue? (Y/N): ")


main()
