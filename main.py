from grid import grid
from solver import solver
from show_grid import show_grid
import numpy as np

grid = grid()


show_grid(grid)


solver(grid)
print('------------')

show_grid(grid)

