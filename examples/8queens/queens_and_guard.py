# Object-oriented solution to the 8 Queens puzzle ported from Smalltalk
# example in chapter 6 of "An Introduction to Object-Oriented Programming"
# (3rd ed.) by Timothy Budd


def aligned(source: tuple, target: tuple) -> bool:
    """True if positions are aligned orthogonally or diagonally."""
    row, col = source
    target_row, target_col = target
    if row == target_row or col == target_col:
        return True
    # test diagonals
    delta = row - target_row
    if (col + delta == target_col) or (col - delta == target_col):
        return True
    return False


def all_safe(positions: list) -> bool:
    """True if none of the positions are aligned."""
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            if aligned(positions[i], positions[j]):
                return False
    return True

class Queen:

    def __init__(self, size, column, neighbor):
        self.size = size
        self.column = column
        self.neighbor = neighbor
        self.row = 1

    def can_attack(self, test_row, test_column) -> bool:
        """True if self or any neighbor can attack."""
        if aligned((self.row, self.column), (test_row, test_column)):
            return True
        # test neighbors
        return self.neighbor.can_attack(test_row, test_column)


    def advance(self) -> bool:
        if self.row < self.size:  # try next row
            self.row += 1
            return self.find_solution()
        
        # cannot go further, move neighbor
        if not self.neighbor.advance():
            return False
        self.row = 1
        return self.find_solution()

    def find_solution(self) -> bool:
        while self.neighbor.can_attack(self.row, self.column):
            if not self.advance():
                return False
        return True

    def result(self) -> list:
        return self.neighbor.result() + [(self.row, self.column)]


class Guard:
    """A sentinel object."""

    def advance(self) -> bool:
        return False

    def can_attack(self, row, column) -> bool:
        return False

    def result(self) -> list:
        return []


def draw_row(size, row, column):
    queen = '│ \N{black chess queen} '
    square = '│   '
    if row == 1:
        print('┌───' + '┬───' * (size-1) + '┐')
    else:
        print('├───' + '┼───' * (size-1) + '┤')
    print(square * (column-1), queen, square * (size-column), '│', sep='')
    if row == size:
        print('└───' + '┴───' * (size-1) + '┘')


class NoSolution(BaseException):
    """No solution found."""


def solve(size):
    figure = Guard()
    for i in range(1, size+1):
        figure = Queen(size, i, figure)
        found = figure.find_solution()
        if not found:
            raise NoSolution()

    return figure.result()


def main(size):
    try:
        result = sorted(solve(size))
    except NoSolution as exc:
        print(exc.__doc__)
    else:
        print(result)
        for cell in result:
            draw_row(size, *cell)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        size = int(sys.argv[1])
    else:
        size = 8
    main(size)
 