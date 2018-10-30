import collections


class Index:
    """An inverted index: maps each key to a set of values."""

    def __init__(self):
        self._map = collections.defaultdict(set)

    def add(self, key, value):
        self._map[key].add(value)

    def __getitem__(self, key):
        return self._map[key]

    def get(self, key, *other_keys):
        """get the intersection of results for the keys"""
        results = self[key]
        for key in other_keys:
            results &= self[key]
        return results
