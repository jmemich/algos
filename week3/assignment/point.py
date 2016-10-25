import numpy as np


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def compare_to(self, point):
        # tie-break with x-axis
        if self.y == point.y:
            return self.x < point.x
        return self.y < point.y

    def slope_to(self, point):
        rise = point.y - self.y
        run = point.x - self.x
        if point.x == self.x and point.y == self.y:
            return -np.inf
        elif run == 0:
            return np.inf
        elif rise == 0:
            return 0
        else:
            return rise / run

    def slope_order(self):
        def slope_comparator(point1, point2):
            slope1 = self.slope_to(point1)
            slope2 = self.slope_to(point2)
            return slope1 < slope2
        return slope_comparator


if __name__ == '__main__':
    p1 = Point(1, 1)
    p2 = Point(2, 2)
    p3 = Point(1, 1.5)
    comparator = p1.slope_order()
    print(comparator(p2, p3))
