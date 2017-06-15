import numpy as np


class QuickFind:

    def __init__(self, n):
        # "constructor"
        self.arr = np.array(range(n))

    def find(self, p):
        return self.arr[p]

    def union(self, p, q):
        p_val = self.arr[p]
        q_val = self.arr[q]
        for i in range(len(self.arr)):
            if self.arr[i] == p_val:
                self.arr[i] = q_val 

    def connected(self, p, q):
        return self.find(p) == self.find(q)


class QuickUnion:

    def __init__(self, N):
        # "constructor"
        self.arr = np.array(range(N))

    def root(self, p):
        while self.arr[p] != p:
            p = self.arr[p]
        return p

    def union(self, p, q):
        # still could have N array accesses
        p_root = self.root(p)
        q_root = self.root(q)
        self.arr[p_root] = q_root

    def connected(seld, p, q):
        return self.root(p) == self.root(q)


class WeightedQuickUnion:

    def __init__(self, N):
        # "constructor"
        self.arr = np.array(range(N))
        self.sz = np.ones(N)

    def root(self, p):
        while self.arr[p] != p:
            p = self.arr[p]
        return p

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return
        if self.sz[p_root] < self.sz[q_root]:
            self.arr[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.arr[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]

    def connected(seld, p, q):
        return self.root(p) == self.root(q)


class QuickUnionPathCompression(WeightedQuickUnion):

    def root(self, p):
        """We can make path compression with root() by implementing a 
        'one-pass' variant such that `self.arr[p] = self.arr[self.arr[p]]`
        and each node points to its grandparent on the way up the tree.
        """
        while self.arr[p] != p:
            self.arr[p] = self.arr[self.arr[p]]
            p = self.arr[p]
        return p

