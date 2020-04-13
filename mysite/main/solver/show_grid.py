def show_grid(grid):
    for row_index, rows in enumerate(grid):
        row_string = '  |  '
        for column_index, cell in enumerate(rows):
            row_string += str(cell) + ' '
            if column_index == 2 or column_index == 5:
                row_string += ' | '
        row_string += '| '
        print(row_string)

        if row_index == 2 or row_index == 5:
            print('-' * len(row_string))
    return None
