def square(grid, cell):
    """
    :param grid: Grid of the Sudoku
    :param cell: Interested cell
    :return: the square of this cels
    """
    selected_rows = find_approapriate_rows(grid, cell[0])
    square = find_approapriate_columns(selected_rows, cell[1])
    return square

def find_approapriate_rows(grid, row):
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]
    if row in first:
        return grid[0:3]
    elif row in second:
        return grid[4:6]
    else:
        return grid[7:9]

def find_approapriate_columns(selected_rows, column):
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]
    if column in first:
        return selected_rows[:, 0:3]
    elif column in second:
        return selected_rows[:, 4:6]
    else:
        return selected_rows[:, 7:9]