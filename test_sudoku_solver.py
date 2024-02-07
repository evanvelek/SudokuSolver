import unittest
from sudoku_solver import solve
from sudoku_solver import is_valid


class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self._board = [
            [3, 0, 0, 0, 4, 0, 0, 7, 0],
            [0, 0, 6, 0, 2, 0, 0, 0, 0],
            [5, 0, 0, 7, 0, 6, 0, 0, 9],
            [0, 0, 5, 3, 0, 1, 0, 2, 0],
            [0, 0, 0, 0, 6, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 3, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 1, 5, 0, 7, 0, 3, 0]
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
        solve(0, 0, self._board)
        self.assertEqual(self._board, [
            [3, 9, 8, 1, 4, 5, 2, 7, 6],
            [7, 4, 6, 9, 2, 3, 1, 8, 5],
            [5, 1, 2, 7, 8, 6, 3, 4, 9],
            [6, 8, 5, 3, 7, 1, 9, 2, 4],
            [1, 2, 4, 8, 6, 9, 7, 5, 3],
            [9, 7, 3, 2, 5, 4, 8, 6, 1],
            [4, 3, 7, 6, 1, 8, 5, 9, 2],
            [8, 5, 9, 4, 3, 2, 6, 1, 7],
            [2, 6, 1, 5, 9, 7, 4, 3, 8]
        ])


if __name__ == '__main__':
    unittest.main()
