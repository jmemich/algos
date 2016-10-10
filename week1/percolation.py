import numpy as np


class WeightedQuickUnionPathCompression:

    def __init__(self, N):
        # "constructor"
        self.arr = np.array(range(N))
        self.sz = np.ones(N)

    def root(self, p):
         while self.arr[p] != p:
             self.arr[p] = self.arr[self.arr[p]]
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

    def connected(self, p, q):
        return self.root(p) == self.root(q)


class Percolation:

    def __init__(self, N, bullshit=False):
        self.N = N
        self.qu = WeightedQuickUnionPathCompression(N * N + 2)
        self.open_id = np.zeros(N * N, dtype='bool')
        self.topv_index = N * N
        self.downv_index = N * N + 1
        self.bullshit = bullshit

    def __repr__(self):
        return str(self.qu.arr[:-2].reshape(self.N, self.N)) + \
            "\n" + \
            str(self.open_id.reshape(self.N, self.N)) + \
            "\nTop virtual index is: {}".format(
                self.qu.arr[self.topv_index]) + \
            "\nDown virtual index is: {}".format(
                self.qu.arr[self.downv_index]) + \
            "\nPercolate is {}".format(self.percolates)

    def convert(self, p):
        i, j = p
        return (i * self.N) + j

    def valid(self, x):
        return x < self.N and x >= 0

    def adjacent(self, p):
        i, j = p
        return ((i-1, j), (i, j+1), (i+1, j), (i, j-1))

    def open(self, p):
        # zero-indexing stupidity
        if self.bullshit:
            p = (p[0] - 1, p[1] - 1) 
        if self.is_open(p):
            return
       
        i, j = p
        index_1d = self.convert(p)
        
        if i == 0 and self.valid(j):
            self.qu.union(self.topv_index, index_1d)
        if i == self.N - 1 and self.valid(j): 
            self.qu.union(self.downv_index, index_1d)     
        
        self.open_id[index_1d] = True

        for cell in self.adjacent(p):
            if self.valid(cell[0]) and self.valid(cell[1]):
                if self.is_open(cell):
                    cell_index_1d = self.convert(cell)
                    self.qu.union(cell_index_1d, index_1d)

    def is_open(self, p):
        index_1d = self.convert(p)
        return self.open_id[index_1d]

    def is_full(self, p):
        # not used?
        index_1d = self.convert(p)
        return not self.open_id[index_1d]

    @property
    def percolates(self):
        return self.qu.connected(self.topv_index, self.downv_index)


if __name__ == '__main__':
    p = Percolation(2, bullshit=True)
    p.open((1,1))
    p.open((2,2))
    p.open((1,2))
    print(p)
