"""
Class ``IBingo`` is an iterable that yields items at random from
a collection of items, like to a bingo cage.

To create an ``IBingo`` instance, provide an iterable with the items::

    >>> balls = set(range(3))
    >>> cage = IBingo(balls)

The instance is iterable::

    >>> results = [item for item in cage]
    >>> sorted(results)
    [0, 1, 2]

Iterating over an instance does not change the instance. Each iterator
has its own copy of the items. If ``IBingo`` instances were changed on
iteration, the value of this expression would be 0 (zero)::

    >>> len([item for item in cage])
    3

"""

import bingo


class IBingo(bingo.Bingo):

    def __iter__(self):
        """return generator to yield items one by one"""
        items = self._items[:]
        while items:
            yield items.pop()
