import numpy as np


def binary_knapsack_solver(profit, weight, total):
    """simple 0-1 knapsack solver"""

    solution_items = []
    solution_weight = 0

    value = np.divide(profit, weight)

    while solution_weight <= total:

        # sort order
        value_index = value.argsort().tolist()

        # add item if not breaking total constraint
        while value_index:
            i = value_index.pop()  # NOTE takes from LHS
            if not solution_weight + weight[i] > total:
                solution_items.append(i)
                solution_weight += weight[i]
            else:
                return solution_items

def continuous_knapsack_solver(profit, weight, total):
    """ 
    continuous knapsack solver
    
    notation from:
        http://www.or.deis.unibo.it/kp/Chapter2.pdf (p.18)
    """

    assert len(profit) == len(weight)
    n = len(profit)

    c = total
    p = np.array(profit)
    w = np.array(weight)

    J0 = set()
    J1 = set()
    JC = set(range(n))

    c_bar = c
    partition = False

    while not partition:

        # subset to remaining values
        _p = p[list(JC)]
        _w = w[list(JC)]
        R = np.divide(_p, _w)
        l = np.median(R)

        # indices
        G = np.flatnonzero(R > l)
        L = np.flatnonzero(R < l)
        E = np.flatnonzero(R == l)

        c_ = _w[G].sum()
        c__ = c_ + _w[E].sum()

        if c_ <= c_bar < c__:
            partition = True
        else:
            if c_ > c_bar:
                # l is too small!
                J0 = J0.union(set(L).union(set(E)))
                JC = set(G)
            else:
                # l is too large!
                J1 = J1.union(set(G).union(set(E)))
                JC = set(L)
                c_bar = c_bar - c__

    J1 = J1.union(set(G))
    J0 = J0.union(set(L))
    JC = set(E)

    """ This is to find critical value!
    c_bar = c_bar - c_

    # find smallest candidate weight value above `c_bar`; return index
    cand = w[list(JC)]
    val = min(cand[cand > c_bar])
    sigma = np.array(list(JC))[cand == val]
    """

    # really, we want to return the set of items we should add to knapsack
    return J1


if __name__ == '__main__':

    profit = [10, 11, 21, 13, 14, 15, 20, 30, 35]
    weight = [2, 20, 30, 15, 29, 29, 110, 11, 17]
    total_weight = 59

    result = continuous_knapsack_solver(profit, weight, total_weight)
    print(result)
