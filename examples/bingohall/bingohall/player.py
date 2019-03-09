from random import randint


class Card:

    size = 5

    @classmethod
    def max_number(cls):
        return cls.size * cls.size * 3

    def __init__(self, randint=randint):
        selected = set()
        size = Card.size
        while len(selected) < size * size:
            selected.add(randint(1, Card.max_number()))
        numbers = sorted(list(selected))
        self.rows = [numbers[i::size] for i in range(size)]

    def __str__(self):
        lines = []
        for row in self.rows:
            line = []
            for space in row:
                line.append(f'{space:2d}')
            lines.append(' '.join(line))
        return '\n'.join(lines)
