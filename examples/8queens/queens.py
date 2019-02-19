# An Object-oriented solution to the 8 Queens puzzle ported from Smalltalk
# example in chapter 6 of "An Introduction to Object-Oriented Programming"
# (3rd ed.) by Timothy Budd


class Queen:

    def __init__(self, column, neighbor):
        self.column = column
        self.neighbor = neighbor
        self.row = 1

    def can_attack(self, row, column) -> bool:
        """True if self or neighbor(s) can attack row, column"""
        if row == self.row:
            return True
        # test diagonals
        delta = column - self.column
        if (self.row + delta == row) or (self.row - delta == row):
            return True
        # test neighbors
        return self.neighbor.can_attack(row, column)

    def advance(self) -> bool:
        if self.row < N:  # try next row
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


class Sentinel:
    def advance(self):
        return False

    def can_attack(self, row, column):
        return False

    def result(self):
        return []


def draw_row(row, column):
    queen = '│ \N{black chess queen} '
    square = '│   '
    if row == 1:
        print('┌───' + '┬───' * (N-1) + '┐')
    else:
        print('├───' + '┼───' * (N-1) + '┤')
    print(square * (column-1), queen, square * (N-column), '│', sep='')
    if row == N:
        print('└───' + '┴───' * (N-1) + '┘')


def main():
    last_queen = Sentinel()
    for i in range(1, N+1):
        last_queen = Queen(i, last_queen)
        last_queen.find_solution()

    result = sorted(last_queen.result())
    print(result)
    for cell in result:
        draw_row(*cell)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    else:
        N = 8
    main()
 