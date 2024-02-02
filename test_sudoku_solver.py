import unittest
from sudoku_solver import solve
from sudoku_solver import is_valid


class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self._board = [
            [0, 0, 6, 0, 0, 0, 9, 0, 0],
            [0, 0, 0, 0, 2, 1, 0, 4, 8],
            [0, 1, 0, 4, 9, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 4, 0, 5],
            [0, 4, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 1, 7, 0, 0, 0, 9, 6],
            [1, 7, 0, 5, 4, 0, 8, 6, 4],
            [5, 6, 0, 0, 0, 8, 0, 0, 0],
            [9, 3, 0, 2, 7, 6, 1, 0, 4]
        ]
    def test_valid_board_checker_finds_doubles_in_same_row(self):
        self._board[0][0] = 6
        self.assertEqual(is_valid(0, 0, self._board), False)

    def test_valid_board_checker_finds_doubles_in_same_col(self):
        self._board[0][0] = 9
        self.assertEqual(is_valid(0, 0, self._board), False)

    def test_valid_board_checker_finds_doubles_in_same_box(self):
        self._board[0][3] = 6
        self.assertEqual(is_valid(0, 0, self._board), False)

    def test_valid_board_checker_returns_true_with_valid_board(self):
        self.assertEqual(is_valid(0, 2, self._board), True)


    def test_sudoku_solver_works_as_a_whole(self):
        self.assertEqual(solve(0, 0, self._board), [
            [4, 2, 6, 8, 3, 5, 9, 7, 1],
            [7, 9, 3, 6, 2, 1, 5, 4, 8],
            [8, 1, 5, 4, 9, 7, 6, 3, 2],
            [2, 8, 7, 9, 6, 3, 4, 1, 5],
            [6, 4, 9, 1, 5, 2, 3, 8, 7],
            [3, 5, 1, 7, 8, 4, 2, 9, 6],
            [1, 7, 2, 5, 4, 9, 8, 6, 4],
            [5, 6, 4, 3, 1, 8, 7, 2, 9],
            [9, 3, 8, 2, 7, 6, 1, 5, 4]
        ])


if __name__ == '__main__':
    unittest.main()
