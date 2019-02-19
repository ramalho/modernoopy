# Object-oriented solution to the 8 Queens puzzle ported from Object Pascal
# example in chapter 6 of "An Introduction to Object-Oriented Programming"
# (3rd ed.) by Timothy Budd


class Queen:

    def __init__(self, column, neighbor):
        self.column = column
        self.neighbor = neighbor
        self.row = 1

    def can_attack(self, test_row, test_col):
        if self.row == test_row:
            return True

        delta = test_col - self.column
        if ((self.row + delta == test_row) or
            (self.row - delta == test_row)):
            return True

        if self.neighbor:
            return self.neighbor.can_attack(test_row, test_col)

    def find_solution(self):
        if self.neighbor:
            while self.neighbor.can_attack(self.row, self.column):
                if not self.advance():
                    return False
        return True

    def advance(self):
        if self.row < N:
            self.row += 1
            return self.find_solution()
        if self.neighbor:
            if not self.neighbor.advance():
                return False
            else:
                self.row = 1
                return self.find_solution()
        return False

    def locate(self):
        if not self.neighbor:
            return [(self.row, self.column)]
        else:
            return self.neighbor.locate() + [(self.row, self.column)]


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
    neighbor = None
    for i in range(1, N+1):
        last_queen = Queen(i, neighbor)
        if not last_queen.find_solution():
            print('no solution')
        neighbor = last_queen

    places = sorted(last_queen.locate())
    print(places)
    for cell in places:
        draw_row(*cell)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    else:
        N = 8
    main()
