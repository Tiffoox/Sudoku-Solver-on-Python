from grid import grid
import numpy as np

grid = grid()

for index_row in range(9):
    for index_column in range(9):
        row = list(grid[index_row, :])
        column = list(grid[:, index_column])
        square = grid[0:3, 0:3]
        square = list(np.array(square).flatten())


        grid_cell = grid[index_row, index_column]
        possible_numbers = []
        for number in range(9):
            if grid_cell == "":
                if grid_cell not in row and grid_cell not in column and grid_cell not in square:
                    possible_numbers.append(number)
        if len(possible_numbers) == 1:
            grid[index_row, index_column] = possible_numbers[0]
