import numpy as np
from point import Point
from line import LineSegment
from itertools import combinations


class BruteCollinearPoints:

    def __init__(self, points, n_collinear=4):
        assert len(points) >= n_collinear, ('Number of points examined '
                                            'at a time greater than total')
        self.points = points
        self.n_points = len(points)
        self.n_collinear = n_collinear

    def longest_segment(self, points_list):
        # dirty hack -- fine as long as origin isn't in `points_list`
        origin = Point(1000000, 10000001)
        slopes = []
        for point in points_list:
            slopes.append(origin.slope_to(point))
        return LineSegment(points_list[slopes.index(min(slopes))],
                           points_list[slopes.index(max(slopes))])

    def collinear_points(self):
        segments = []
        # non-itertools equivalent here runs in n^4 worst case
        for candidate in combinations(self.points, self.n_collinear):
            base = candidate[0]
            slopes = []
            for point in candidate[1:self.n_collinear]:
                slopes.append(base.slope_to(point))
            if len(set(slopes)) == 1:
                segment = self.longest_segment(candidate)
                if segment not in segments:
                    segments.append(segment)
        return segments


if __name__ == '__main__':
    points = [Point(1, 1), Point(1, 2),
              Point(2, 2), Point(2, 3),
              Point(3, 3), Point(3, 4),
              Point(4, 4), Point(4, 5),
              Point(5, 5), Point(3, 9)]
    b = BruteCollinearPoints(points)
    result = b.collinear_points()
    print(result)
    import ipdb; ipdb.set_trace()
