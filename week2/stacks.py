import numpy as np

class LinkedStackOfStrings:

    class Node:

        def __init__(self, item, next):
            self.item = item 
            self.next = next 

    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first == None

    def push(self, item):
        old_first = self.first
        self.first = self.Node(item, old_first)

    def pop(self):
        string = self.first.item
        self.first = self.first.next
        return string


class FixedCapacityStackOfStrings:
    # This is less memory than strings?! (Java numbers...)
    # NOTE: worst case takes time proportional to N, due to resize()

    def __init__(self, capacity):
        self.N = 0 
        self.s = np.ndarray(capacity, dtype='object')

    def is_empty(self):
        return self.N == 0

    def push(self, item):
        self.N += 1
        self.s[self.N] = item

    def pop(self):
        # deal with loitering: remove array value which cannot be referenced
        self.N -= 1
        item = self.s[self.N]
        self.s[self.N] = None
        return item


class ResizingArrayStackOfStrigns(FixedCapacityStackOfStrings):

    def __init__(self):
        self.N = 0
        self.s = np.ndarray(1, dtype='object')

    def push(self, item):
        if self.N + 1 == len(self.s):
            self.resize(2 * len(self.s))
        self.N += 1
        self.s[self.N] = item

    def resize(self, capacity):
        copy = np.ndarray(capacity, dtype='object')
        for i in range(len(self.s)):
            copy[i] = self.s[i]
        self.s = copy

    def pop(self):
        # deal with loitering: remove array value which cannot be referenced
        self.N -= 1
        item = self.s[self.N]
        self.s[self.N] = None
        # efficient solution to reduce size. prevents 'thrashing' where
        # sequence push-pop-push-pop when the array is full means that
        # every operation takes time proportional to N.
        if self.N > 0 and self.N == len(self.s) / 4:
            self.resize(len(self.s) / 2)
        return item


