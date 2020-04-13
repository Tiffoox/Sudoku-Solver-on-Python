from grid import grid
from mysite.main.solver.solver import solver
from mysite.main.solver.show_grid import show_grid

grid = grid()


show_grid(grid)


solver(grid)
print('------------')

show_grid(grid)

