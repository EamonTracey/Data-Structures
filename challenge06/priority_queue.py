#!/usr/bin/env python3

'''
Title:      priority_queue.py
Abstract:   Implement a priority queue using a binary heap.
Author:     Eamon Tracey
Email:      etracey@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questiones:

    1. What is the worst-case time complexity of PriorityQueue.push()?

        O(log(n))

    2. What is the worst-case time complexity of PriorityQueue.pop()?

        O(log(n))

    3. How did you work around the fact that heapq is a min-heap, while our
    PriorityQueue is a max-heap?

        To work around the fact that heapq is a min-heap, I internally
        multiply each of the data values by -1. This effectively
        reverses the order of smallest-to-largest values. When inserting
        a new value, I insert the negative of the value. Similarly, when
        popping a value, I return the negative of the stored value, thus
        returning the desired maximum value.
'''

import heapq

# Classes


class PriorityQueue:
    ''' Simple priority queue based on a binary heap. '''

    def __init__(self, data=None):
        ''' Initialize the internal data.

        >>> pq = PriorityQueue(); pq.data
        []

        >>> pq = PriorityQueue([3, 1, 4]); pq.data[0]
        -4
        '''
        self.data = data or []
        self.data = [-value for value in self.data]
        heapq.heapify(self.data)

    def push(self, item):
        ''' Add item to Priority Queue.

        >>> pq = PriorityQueue(); pq.push(3); pq.data[0]
        -3

        >>> pq.push(1); pq.data[0]
        -3

        >>> pq.push(4); pq.data[0]
        -4
        '''
        heapq.heappush(self.data, -item)

    def pop(self):
        ''' Remove and return smallest value from the Priority Queue.
        >>> pq = PriorityQueue([3, 1 ,4]); pq.pop()
        4

        >>> pq.pop()
        3

        >>> pq.pop()
        1
        '''
        return -heapq.heappop(self.data)

    def size(self):
        ''' Return number of values in Priority Queue.

        >>> pq = PriorityQueue(); pq.size()
        0

        >>> pq = PriorityQueue([3, 1, 4]); pq.size()
        3
        '''
        return len(self.data)
