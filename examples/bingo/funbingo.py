"""
Function ``funbingo`` returns a closure that picks an item
at random from a collection of items, removing the item
from the collection, like to a bingo cage.

To create a loaded instance, provide an iterable with the items::

    >>> balls = set(range(3))
    >>> enclosure = funbingo(balls)

Invoking the closure retrieves an item at random, removing it::

    >>> b1 = enclosure()
    >>> b2 = enclosure()
    >>> b3 = enclosure()
    >>> balls == {b1, b2, b3}
    True

"""

import random

def funbingo(items):
    items = list(items)
    random.shuffle(items)

    def popper():
        return items.pop()

    return popper
