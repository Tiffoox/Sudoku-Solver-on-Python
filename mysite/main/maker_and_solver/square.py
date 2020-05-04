def square(grid, cell):
    """
    :param grid: Grid of the Sudoku
    :param cell: Interested cell
    :return: the square of this cels
    """
    rows = (cell[0] // 3) * 3
    columns = (cell[1] // 3) * 3

    return grid[rows:rows+3, columns:columns+3]