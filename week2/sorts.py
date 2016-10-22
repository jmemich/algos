import numpy as np

# sort should be blind to data type...
# hack magic methods? unecessary?

# method: less()
# method: exchange()


class SelectionSort:

    def less(self, a, b):
        return a < b

    def exch(self, arr, a, b):
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

    def sort(self, arr):
        N = len(arr)
        for i in range(N):
            min = i
            for j in range(i + 1, N):
                if self.less(arr[j], arr[min]):
                    min = j
            self.exch(arr, i, min)


class InsertionSort:

    def less(self, a, b):
        return a < b

    def exch(self, arr, a, b):
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

    def sort(self, arr):
        N = len(arr)
        for i in range(0, N):
            for j in range(0, i):
                inner = i - j - 1
                if self.less(arr[i], arr[inner]):
                    self.exch(arr, inner, i)
                else:
                    break


class ShellSort:

    def sort(self, arr):
        # https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Shell_sort#Python
        N = len(arr)
        gap = 1
        while (gap < N / 3):
            # 3x + 1 increment sequence
            gap = 3 * gap + 1
        while gap > 0:
            for i in range(gap, N):
                val = arr[i]
                j = i
                while j >= gap and arr[j - gap] > val:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = val
            gap //= 3


if __name__ == '__main__':
    a = np.array([2,1,3,5,4,8,9,0])
    print(a)
    s = ShellSort()
    s.sort(a)
    print(a)
