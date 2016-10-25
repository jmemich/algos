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
        # divide and conquer!
        if high <= low:
            # could but insertion sort here for small sub-arrays!
            # it's much more efficient than the recursive call
            return
        mid = low + (high - low) // 2
        self._sort(arr, aux, low, mid)
        self._sort(arr, aux, mid + 1, high)
        # we can add check here to test if largest element of 'low' 
        # array is smaller than smallest elemnt of 'high' array -- we then
        # know we've already sorted it!
        if arr[mid + 1] >= arr[mid]:
            return
        self.merge(arr, aux, low, mid, high)

    def sort(self, arr):
        # create aux array here, don't need to dupe inside `_sort`
        aux = np.zeros(len(arr), dtype='uint8')
        self._sort(arr, aux, 0, len(arr) - 1)


class BottomUpMergeSort:

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

    def sort(self, arr):
        aux = np.zeros(len(arr), dtype='uint8')
        N = len(arr)
        sz = 1
        while sz < N:
            low = 0
            while low < N - sz:
                mid = low + sz - 1
                high = min(low + sz + sz - 1, N - 1)
                self.merge(arr, aux, low, mid, high)
                low += sz + sz
            sz += sz


if __name__ == '__main__':
    arr = np.array([0,1,1,5,0,4,8,9])
    print(arr)
    m = MergeSort()
    m.sort(arr)
    print(arr)

    arr = np.array([0,1,1,5,0,4,8,9])
    print(arr)
    bu = BottomUpMergeSort()
    bu.sort(arr)
    print(arr)
