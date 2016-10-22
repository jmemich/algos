import numpy as np


class MergeSort:
    
    def is_sorted(self, arr):
        i = 0
        while i < len(arr) - 1:
            if not arr[i] <= arr[i + 1]:
                return False
            i += 1
        return True

    def merge(self, arr, aux, low, mid, high):
        
        assert self.is_sorted(arr[low:mid])
        assert self.is_sorted(arr[mid + 1:high])

        for i in range(high + 1):
            aux[i] = arr[i]

        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > high:
                arr[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                # could use less() here
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1
        
        assert self.is_sorted(arr[low:high])

    def _sort(self, arr, aux, low, high):
        if high <= low:
            return
        mid = low + (high - low) // 2
        self._sort(arr, aux, low, mid)
        self._sort(arr, aux, mid + 1, high)
        self.merge(arr, aux, low, mid, high)

    def sort(self, arr):
        # create aux array here, don't need to dupe inside `_sort`
        aux = np.zeros(len(arr), dtype='uint8')
        self._sort(arr, aux, 0, len(arr) - 1)

if __name__ == '__main__':
    arr = np.array([0,1,3,5,0,4,8,9])
    print(arr)
    m = MergeSort()
    m.sort(arr)
    print(arr)
