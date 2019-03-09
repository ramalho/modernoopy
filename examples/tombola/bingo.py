"""
Class ``Bingo`` picks an item at random from a collection of items,
removing the item from the collection, like to a bingo cage.

To create a loaded instance, provide an iterable with the items::

    >>> balls = set(range(3))
    >>> cage = Bingo(balls)

The ``pop`` method retrieves an item at random, removing it::

    >>> b1 = cage.pop()
    >>> b2 = cage.pop()
    >>> b3 = cage.pop()
    >>> balls == {b1, b2, b3}
    True

The ``__len__`` method reports the number of items available,
which makes ``Bingo`` instances compatible with the ``len`` and
``bool`` built-in functions::

    >>> len(cage)
    0
    >>> bool(cage)
    False

``bool`` is rarely called directly as above, but useful for use
with ``if`` and ``while``. For example:

    >>> if cage:
    ...    print('Next item:', cage.pop())
    ... else:
    ...    print('No more items available.')
    ...
    No more items available.


Now testing ``__len__`` with a loaded ``cage``::

    >>> cage = Bingo(balls)
    >>> len(cage)
    3
    >>> bool(cage)
    True
    >>> results = []
    >>> while cage:
    ...     results.append(cage.pop())
    ...
    >>> len(results)
    3

"""

import random


class Bingo:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)
