def square(grid, cell):
    """
    :param grid: Grid of the Sudoku
    :param cell: Interested cell
    :return: the square of this cels
    """
    appropriate_rows = find_approapriate_vector(cell[0])
    appropriate_columns = find_approapriate_vector(cell[1])
    square = grid[appropriate_rows, appropriate_columns]
    return square

def find_approapriate_vector(value):
    first = [0, 1 ,2]
    second = [3, 4, 5]
    third = [6, 7, 8]
    if value in first:
        return first
    elif value in second:
        return second
    else:
        return third