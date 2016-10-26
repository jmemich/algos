class LineSegment:

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __repr__(self):
        return 'LineSegment({}, {})'.format(self.p, self.q)

    def __eq__(self, segment):
        p1, q1 = self.p, self.q
        p2, q2 = segment.p, segment.q
        if p1.compare_to(q1) and p2.compare_to(q2):
            # p1, p2 are smallest points
            if ((p1.x == p2.x and p1.y == p2.y) and
                (q1.x == q2.x and q1.y == q2.y)):
                    return True
            return False
        elif p1.compare_to(q1) and q2.compare_to(p2):
            # p1, q2 are smallest points
            if ((p1.x == q2.x and p1.y == q2.y) and
                (q1.x == p2.x and q1.y == p2.y)):
                    return True
            return False
        elif q1.compare_to(p1) and p2.compare_to(q2):
            # q1, p2 are smallest points
            if ((q1.x == p2.x and q1.y == p2.y) and
                (q2.x == p1.x and q2.y == p1.y)):
                    return True
            return False
        else:
            # equality!
            if ((p1.x == p2.x and p1.y == p2.y) and
                (q1.x == q2.x and q1.y == q2.y)):
                    return True
            elif ((p1.x == q2.x and p1.y == q2.y) and
                  (q1.x == p2.x and q1.y == p2.y)):
                    return True
            else:
                return False
