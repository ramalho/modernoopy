import pytest

@pytest.fixture
def board():
    return [
        [1, 1, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]


@pytest.fixture
def board_mirrored():
    return [
        [0, 1, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]


def complete_column(board, column):
    return all(row[column] for row in board)


def complete_row(board, row):
    return all(board[row])


def complete_diagonal(board, row, column):
    size = len(board)  # assume square board
    if row == column:
        return all(board[i][i] for i in range(size))
    elif row == (size - column - 1):
        return all(board[i][size - i - 1] for i in range(size))


def test_complete_column(board):
    assert complete_column(board, 1)


def test_complete_column_false(board):
    assert not complete_column(board, 2)


def test_complete_row(board):
    assert complete_row(board, 2)


def test_complete_row_false(board):
    assert not complete_row(board, 1)


def test_complete_diagonal(board):
    assert complete_diagonal(board, 1, 1)


def test_complete_diagonal_mirrored(board_mirrored):
    assert complete_diagonal(board_mirrored, 1, 1)

