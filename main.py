from grid import grid
from square import square
import numpy as np
grid = grid()
x = []
for index_row in range(9):
    for index_column in range(9):
        #find the corresponding row, column and square of the cell
        row = list(grid[index_row, :])
        column = list(grid[:, index_column])
        current_square = square(grid, [index_row, index_column])
        x.append(current_square)

        #return the value of the square in a list
        current_square = list(np.array(current_square).flatten())

        grid_cell = grid[index_row, index_column]
        possible_numbers = []
        for number in range(9):
            if grid_cell == "":
                if grid_cell not in row and grid_cell not in column and grid_cell not in current_square:
                    possible_numbers.append(number)

        if len(possible_numbers) == 1:
            grid[index_row, index_column] = possible_numbers[0]
