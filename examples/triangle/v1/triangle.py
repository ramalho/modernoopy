"""
Simple class to represent a right-angled triangle.

    >>> t = RightTriangle(3, 4)
    >>> t.a
    3.0
    >>> t.hypot()
    5.0
    >>> t.display()
    Right triangle with sides 5.0, 4.0, and 3.0.
    >>> t  # doctest:+ELLIPSIS
    <triangle.RightTriangle object at 0x...>

"""


import math

class RightTriangle:

    def __init__(self, leg_a, leg_b):
        self.a = float(leg_a)
        self.b = float(leg_b)

    def hypot(self):
        return math.hypot(self.a, self.b)

    def display(self):
        sides = [self.a, self.b, self.hypot()]
        sides.sort(reverse=True)
        print("Right triangle with sides {}, {}, and {}."
            .format(*sides))
