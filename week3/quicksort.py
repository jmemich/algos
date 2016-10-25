import numpy as np


class QuickSort:

    def less(self, a, b):
        return a < b

    def exch(self, arr, a, b):
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

    def partition(self, arr, low, high):
        i = low + 1
        j = high
        while True:
            
            while self.less(arr[i], arr[low]):
                i += 1
                if i >= high:
                    break

            while self.less(arr[low], arr[j]):
                j -= 1
                if j <= low:
                    break

            if i >= j:
                break

            self.exch(arr, i, j)
        
        self.exch(arr, low, j)
        return j

    def _sort(self, arr, low, high):
        if high <= low:
            return
        j = self.partition(arr, low, high)
        self._sort(arr, low, j - 1)
        self._sort(arr, j + 1, high)

    def sort(self, arr):
        # shuffle! (assume random...)
        self._sort(arr, 0, len(arr) - 1)



if __name__ == '__main__':
    arr = np.array([8, 2, 1, 4, 3, 7, 9, 0])
    print(arr)
    q = QuickSort()
    q.sort(arr)
    print(arr)
