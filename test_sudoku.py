from unittest import TestCase
import numpy as np
from sudoku import Sudoku

grid = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                 [6, 0, 0, 1, 9, 5, 0, 0, 0],
                 [0, 9, 8, 0, 0, 0, 0, 6, 0],
                 [8, 0, 0, 0, 6, 0, 0, 0, 3],
                 [4, 0, 0, 8, 0, 3, 0, 0, 1],
                 [7, 0, 0, 0, 2, 0, 0, 0, 6],
                 [0, 6, 0, 0, 0, 0, 2, 8, 0],
                 [0, 0, 0, 4, 1, 9, 0, 0, 5],
                 [0, 0, 0, 0, 8, 0, 0, 7, 9]])

complete = np.array([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]])


class TestSudoku(TestCase):
    def setUp(self):
        self.sud0 = Sudoku(grid)
        self.sud1 = Sudoku(grid)
        self.sud2 = Sudoku(grid)
        self.sud3 = Sudoku(grid)
        self.sud4 = Sudoku(grid)
        self.details0 = np.array([0, 9, 8, 0, 0, 0, 0, 6, 0]), [0, 0, 8, 0, 0, 0, 0, 0, 0], np.array([[5, 3, 0],
                                                                                                      [6, 0, 0],
                                                                                                      [0, 9, 8]])
        self.comp = complete

    def test_get_box(self):
        self.assertTrue(np.array_equal(self.sud0.getBox(2, 2), np.array([[5, 3, 0],
                                                                         [6, 0, 0],
                                                                         [0, 9, 8]])))

    def test_get_details(self):
        self.assertTrue(np.array_equal(self.sud0.getDetails(2, 2)[0], self.details0[0]))
        self.assertTrue(np.array_equal(self.sud0.getDetails(2, 2)[1], self.details0[1]))
        self.assertTrue(np.array_equal(self.sud0.getDetails(2, 2)[2], self.details0[2]))

    def test_update(self):
        self.sud1.update(6, 2, 10)
        self.assertEqual(self.sud1.grid[6, 2], 10)

    def test_quick_solve(self):
        self.sud2.quickSolve()
        self.assertTrue(np.array_equal(self.sud2.grid, self.comp))

    def test_back_track(self):
        self.sud3.backTrack()
        self.assertTrue(np.array_equal(self.sud3.grid, self.comp))

    def test_solve(self):
        self.sud4.solve()
        self.assertTrue(np.array_equal(self.sud4.grid, self.comp))
