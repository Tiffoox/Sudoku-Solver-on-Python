from .square import square
import numpy as np
def solver(grid):
    empty_cell = True

    while empty_cell:
        for index_row in range(9):
            for index_column in range(9):
                # find the corresponding row, column and square of the cell
                row = list(grid[index_row, :])
                column = list(grid[:, index_column])
                current_square = square(grid, [index_row, index_column])

                # return the value of the square in a list
                current_square = list(np.array(current_square).flatten())

                grid_cell = grid[index_row, index_column]
                possible_numbers = []
                # Find possible number in the corresponding cell
                for number in range(1, 10):
                    if grid_cell == 0:
                        if number not in row and number not in column and number not in current_square:
                            possible_numbers.append(number)

                # If there is only one possible numbr --> Put it on the grid
                if len(possible_numbers) == 1:
                    grid[index_row, index_column] = possible_numbers[0]

        empty_cell = 0 in grid
    return grid