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


class ResizingArrayStackOfStrings:

    def __init__(self):
        self.N = 0
        self.s = np.ndarray(1, dtype='object')

    def is_empty(self):
        return self.N == 0

    @property
    def size(self):
        return len(self.s)

    def push(self, item):
        if self.N == self.size:
            self.resize(2 * self.size)
        self.s[self.N] = item
        self.N += 1

    def resize(self, capacity):
        copy = np.ndarray(int(capacity), dtype='object')
        for i in range(self.N):
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
        if self.N > 0 and self.N == self.size / 4:
            self.resize(self.size / 2)
        return item


def djikstras_two_stack_string(string):
    #ops = LinkedStackOfStrings()
    #vals = LinkedStackOfStrings()
    ops = ResizingArrayStackOfStrings()
    vals = ResizingArrayStackOfStrings()

    # doesn't use stdin
    for s in string:
        if s == '(':
            pass
        elif s == '+':
            ops.push(s)
        elif s == '*':
            ops.push(s)
        elif s == ')':
            op = ops.pop()
            if op == '+':
                vals.push(vals.pop() + vals.pop())
            elif op == '*':
                vals.push(vals.pop() * vals.pop())
        elif s != ' ':
            vals.push(int(s))
    print(vals.pop())

if __name__ == '__main__':
    s = '( 1 + ( 2 * 3 ) )'
    djikstras_two_stack_string(s)

