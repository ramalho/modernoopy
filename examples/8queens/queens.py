# An Object-oriented solution to the 8 Queens puzzle ported from Smalltalk
# example in chapter 6 of "An Introduction to Object-Oriented Programming"
# (3rd ed.) by Timothy Budd


class Queen:

    def __init__(self, column, neighbor):
        self.column = column
        self.neighbor = neighbor
        self.row = 1

    def safe(self, row, column):
        """True if self and neighbor cannot be attacked from row, column"""
        if row == self.row:
            return False
        # test diagonals
        row_delta = abs(row - self.row)
        column_delta = abs(column - self.column)
        if row_delta == column_delta:
            return False
        # test neighbors
        return self.neighbor.safe(row, column)

    def advance(self):
        if self.row < 8:  # try next row
            self.row += 1
            return self.find_solution()
        else:  # cannot go further, move neighbor
            if not self.neighbor.advance():
                return False
        self.row = 1
        self.find_solution()

    def find_solution(self):
        while not self.neighbor.safe(self.row, self.column):
            if not self.advance():
                return False
        return True

    def result(self):
        return self.neighbor.result() + [(self.row, self.column)]


class Sentinel:
    def advance(self):
        return False

    def safe(self, row, column):
        return True

    def result(self):
        return []


def draw_row(row, column):
    queen = '│ \N{black chess queen} '
    square = '│   '
    if row == 1:
        print('┌───┬───┬───┬───┬───┬───┬───┬───┐')
    else:
        print('├───┼───┼───┼───┼───┼───┼───┼───┤')
    print(square * (column-1), queen, square * (8-column), '│', sep='')
    if row == 8:
        print('└───┴───┴───┴───┴───┴───┴───┴───┘')


def main():
    last_queen = Sentinel()
    for i in range(1, 9):
        last_queen = Queen(i, last_queen)
        last_queen.find_solution()

    result = sorted(last_queen.result())
    print(result)
    for cell in result:
        draw_row(*cell)


if __name__ == '__main__':
    main()
