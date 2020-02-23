""" sudoku.py
Uses an OOP approach to solving Sudoku puzzles using numpy, two different but complementary methods are used.
Uses a traditional 'human-like' solving method named guickSolve() which works in the way a human would work through a
sudoku by filling in cells which only have one possible solution and then looping through this method until complete.
The second method uses backtracking named solve() and takes longer but can solve all puzzle difficulties and works
through each value in a backtracking method. The speed of this method could be improved could be improved.

For a fullSolve() method the puzzle is attempted to be solved with the quickSolve() method, but if this fails the
backtracking method cleans up any remaining empty cells. This is more efficient than running solve() alone.
"""

import numpy as np
from collections import Counter
from datetime import datetime as dt


def empty_list(grid):
    """
    :param grid: sudoku grid
    :return: returns a list row and column tuples which have 0 as a value
    """
    res = np.where(grid == 0)
    r = res[0]
    c = res[1]

    return [(r[i], c[i]) for i in range(len(r))]


def getDetails(grid, row, col):
    """
    :param grid: the sudoku grid to check
    :param row: the row the value is
    :param col: the column the value is in
    :return: three arrays where the value is situated, the row, the column and the grid array
    """
    res_row = grid[row]
    res_col = [i[col] for i in grid]
    res_box = getBox(grid, row, col)
    return res_row, res_col, res_box


def getBox(grid, row, col):
    """
    :param grid: the sudoku grid to check
    :param row: the row the value is
    :param col: the column the value is in
    :return: returns the 3x3 array which the coordinate is situated in
    """
    sep = [0, 3, 6, 9]
    ri = row // 3
    ci = col // 3

    return grid[sep[ri]:sep[ri + 1], sep[ci]:sep[ci + 1]]


def possibleValues(grid, row, col):
    """
    :param grid: the sudoku grid to check
    :param row: the row the value is
    :param col: the column the value is in
    :return: returns an array of possible values which could be placed in that cell
    """
    possible = []
    for d in getDetails(grid, row, col):
        possible.extend([i for i in range(1, 10) if i not in d])
    counter = Counter(possible)
    result = [i for i in counter.keys() if counter[i] == 3]
    return result


def solve(grid):
    """
    Back tracking method for filling a sudoku. This is the 'brute force' method and works through each row
    :param grid: the sudoku grid to solve
    :return: When complete the grid is overwriten with a completed sudoku
    """
    empties = empty_list(grid)
    if not empties:
        return True
    else:
        row, col = empties[0]

    for i in range(1, 10):
        # only checks possible values to limit the number of values checked
        if i in possibleValues(grid, row, col):
            grid[row][col] = i
            if solve(grid):
                return True
            # If the value does not work it is reverted back to 0
            grid[row][col] = 0

    return False


class Sudoku:
    def getBox(self, row, col):
        """Applies function as method"""
        return getBox(self.grid, row, col)

    def getDetails(self, row, col):
        """Applies function as method"""
        return getDetails(self.grid, row, col)

    def update(self, row, col, value):
        """
        :param row: row of the value to be overwritten
        :param col: column of the value to be overwritten
        :param value: the value to be written
        :return: Overwrites the current value with the updated value.
                Also updates the emptyCoords and emptyCount attributes
        """
        self.grid[row, col] = value
        self.emptyCoords = empty_list(self.grid)
        self.emptyCount = len(self.emptyCoords)

    def quickSolve(self):
        """
        Solves the cells which only have one possible solution and then looping through this method recursively until
        complete. Does this by checking which values are possible in each cell and if there is only one solution this is
        the value chosen.
        :return: Updates the grid with these values and produces a log of the results
        """
        empt = [self.emptyCount]
        comp = 'Pass'
        start = dt.now()
        while empt[-1] > 0:
            lastEmpt = empt[-1]
            # work through empty coordinates and update where only one result is possible
            for c, r in self.emptyCoords:
                value = possibleValues(self.grid, c, r)
                if len(value) == 1:
                    self.update(c, r, value[0])
            empt.append(self.emptyCount)
            if empt[-1] == lastEmpt:
                comp = 'Fail'
                break
        # Log the results to the solve_results attr
        resultsLog = {'quick_results': empt,
                      'complete': comp,
                      'quick_complete': comp,
                      'quick_runs': len(empt),
                      'quick_runtime': dt.now() - start}
        self.solve_results.update(resultsLog)

    def backTrack(self):
        """
        Solves the sudoku with the backtracking method, takes longer but is always successful.
        :returns an updated grid attribute and adds results to the solve_results attribute
        """
        grid = self.grid
        start = dt.now()
        res = solve(grid)
        if res:
            # Replace the grid and log the results to the solve_results attr
            self.grid = grid
            resultsLog = {'complete': 'Pass',
                          'backtrack_results': 'Pass',
                          'backtrack_runtime': dt.now() - start}
            self.solve_results.update(resultsLog)

    def solve(self):
        """
        Runs both methods and if quickSolve() does not complete the puzzle the backtracking method is applied to the
        remaining empty cells
        """
        self.quickSolve()
        if self.solve_results['complete'] == 'Fail':
            self.backTrack()

    def __init__(self, grid):
        self.grid = grid
        self.emptyCoords = empty_list(grid)
        self.emptyCount = len(self.emptyCoords)
        self.solve_results = {'complete': 'Fail'}
