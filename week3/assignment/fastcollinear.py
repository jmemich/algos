from point import Point
from line import LineSegment
import numpy as np


class QuickSort:

    def less(self, a, b):
        return a <= b

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


class FastCollinearPoints:

    def __init__(self, points, n_collinear=4):
        self.points = points
        self.n_points = len(points)
        self.n_collinear = n_collinear
        self.quicksort = QuickSort()

    def collinear_points(self):
        for i in range(len(self.points)):
            point = self.points[i]
            segments = [LineSegment(point, q) for q in self.points]
            for s_i in range(len(segments):
                if s_i != i:
                    # TODO 

            slopes = [segment.slope for segment in segments]
            del slopes[i], segments[i]
            self.quicksort.sort(slopes)
            for j in range(len(slopes) - self.n_collinear - 1):
                if set(slopes[j:j+self.n_collinear-1]) == 1:
                    



if __name__ == '__main__':
    points = [Point(1, 1), Point(1, 2),
              Point(2, 2), Point(2, 3),
              Point(3, 3), Point(3, 4),
              Point(4, 4), Point(4, 5),
              Point(5, 5), Point(3, 9)]
    b = FastCollinearPoints(points)
    result = b.collinear_points()
