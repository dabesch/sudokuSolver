import numpy as np
from sudoku import Sudoku

# Sunday times Warm-up sudoku Feb 23rd 2020
stgrid0 = np.array([[0, 0, 3, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 2, 0, 0, 0, 3],
                    [5, 1, 8, 0, 6, 3, 0, 0, 0],
                    [0, 4, 0, 0, 8, 5, 0, 2, 7],
                    [0, 2, 6, 0, 0, 0, 4, 5, 0],
                    [7, 8, 0, 4, 9, 0, 0, 3, 0],
                    [0, 0, 0, 8, 3, 0, 5, 7, 6],
                    [6, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 2, 0, 0]])

# Sunday times Very hard sudoku Feb 23rd 2020
stgrid1 = np.array([[0, 0, 0, 5, 3, 0, 0, 0, 0],
                    [0, 5, 0, 0, 2, 1, 3, 0, 4],
                    [3, 0, 1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 4, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 6, 0, 2, 7, 0, 0],
                    [0, 0, 0, 0, 0, 0, 9, 0, 2],
                    [0, 0, 0, 0, 0, 0, 1, 0, 9],
                    [4, 0, 6, 3, 1, 0, 0, 7, 0],
                    [0, 0, 0, 0, 8, 6, 0, 0, 0]])
# Prize coordinates
prize = [(0, 0), (2, 6), (4, 8)]

sud = Sudoku(stgrid1)
sud.solve()
print(sud.solve_results)
print(sud.grid)
pDigits = [sud.grid[p] for p in prize]
print(f'Prize digits = {pDigits}')
