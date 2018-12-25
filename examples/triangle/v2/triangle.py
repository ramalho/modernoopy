"""
Simple class to represent a right-angled triangle.

    >>> t = RightTriangle(3, 4)
    >>> t.a
    3.0
    >>> t.hypot()
    5.0
    >>> t.area()
    6.0
    >>> t
    RightTriangle(3.0, 4.0)
    >>> str(t)
    'Right triangle with sides 5.0, 4.0, and 3.0.'
    >>> print(t)
    Right triangle with sides 5.0, 4.0, and 3.0.

"""


import math


class RightTriangle:
    def __init__(self, leg_a, leg_b):
        self.a = float(leg_a)
        self.b = float(leg_b)

    def hypot(self):
        return math.hypot(self.a, self.b)

    def area(self):
        return (self.a * self.b) / 2

    def __str__(self):
        sides = [self.a, self.b, self.hypot()]
        sides.sort(reverse=True)
        msg = "Right triangle with sides {}, {}, and {}."
        return msg.format(*sides)

    def __repr__(self):
        return f"RightTriangle({self.a}, {self.b})"
