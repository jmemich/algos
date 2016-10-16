import random
import numpy as np


class Deque:
    """Note: 'fist' == 'left' & 'last' == 'right'"""

    class Node:
        
        def __init__(self, item, left, right):
            self.item = item
            self.left = left
            self.right = right

    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0

    def is_empty(self):
        return self.left == None and self.right == None

    def add_left(self, item):
        if self.is_empty():
            self.left = self.Node(item, None, None)
            self.right = self.left
        else:
            old_left = self.left
            self.left = self.Node(item, None, old_left)
            old_left.left = self.left
        self.size += 1

    def add_right(self, item):
        if self.is_empty():
            self.right = self.Node(item, None, None)
            self.left = self.right
        else:
            old_right = self.right
            self.right = self.Node(item, old_right, None)
            old_right.right = self.right
        self.size += 1

    def remove_left(self):
        item = self.left.item
        if self.left == self.right:
            # last one!
            self.left = None
            self.right = None
        else:
            self.left = self.left.right
        self.size -= 1
        return item

    def remove_right(self):
        item = self.right.item
        if self.left == self.right:
            # last one!
            self.right = None
            self.left = None
        else:
            self.right = self.right.left
        self.size -= 1
        return item

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            # start from left...
            return self.remove_left()


class RandomizedQueue:

    def __init__(self):
        self.N = 0 
        self.s = np.ndarray(1, dtype='object')

    def is_empty(self):
        return self.N == 0 

    @property
    def size(self):
        # note this is size of array, not N items
        return len(self.s)

    def _resize(self, capacity):
        copy = np.ndarray(int(capacity), dtype='object')
        for i in range(self.N):
            copy[i] = self.s[i]
        self.s = copy

    def enqueue(self, item):
        if self.N == self.size:
            self._resize(2 * self.size)
        self.s[self.N] = item
        self.N += 1

    def dequeue(self):
        self.N -= 1
        index = random.randint(0, self.N)  # [0, N]
        item = self.s[index]
        # no need for complex bookkeeping
        self.s[index] = self.s[self.N]
        self.s[self.N] = None
        if self.N > 0 and self.N == self.size / 4:
            self._resize(self.size / 2)
        return item

    def sample(self):
        index = random.randint(0, self.N - 1)
        return self.s[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        else:
            return self.dequeue()
