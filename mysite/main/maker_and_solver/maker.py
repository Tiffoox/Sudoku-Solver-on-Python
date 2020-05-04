from sudoku import Sudoku

import numpy as np
# Initializes a Sudoku puzzle with 3 x 3 sub-grid and
# generates a puzzle with half of the cells empty

def maker():
    puzzle = Sudoku(3).difficulty(0.5)
    grid = np.array(puzzle.board)
    grid = np.where(grid == None, 0, grid)
    return grid

