import collections


class Index:
    """An inverted index. It maps each key to a set of values."""

    def __init__(self):
        self._map = collections.defaultdict(set)

    def add(self, key, value):
        self._map[key].add(value)

    def __getitem__(self, key):
        return self._map[key]
