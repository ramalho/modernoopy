import collections


class Index:
    """An inverted index: maps each key to a set of values."""

    def __init__(self):
        self._map = collections.defaultdict(set)

    def add(self, key, value):
        self._map[key].add(value)

    def __getitem__(self, key):
        return self._map[key]

    def get(self, key, *more_keys):
        """Get the intersection of result sets for each key."""
        result_set = self[key]
        for key in more_keys:
            result_set &= self[key]
        return result_set
