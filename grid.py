import numpy as np

def grid():
    #Give first grid values

    blank = np.NaN

    top_left = ((5, 3, blank), (6, blank, blank), (blank, 9, 8))
    top_center = ((blank, 7, blank), (1, 9, 5), (blank, blank, blank))
    top_right = ((blank, blank, blank), (blank, blank, blank), (blank, 6, blank))

    middle_left = ((8, blank, blank), (4, blank, blank), (7, blank, blank))
    middle_center = ((blank, 6, blank), (8, blank, 3), (blank, 2, blank))
    middle_right = ((blank, blank, 3), (blank, blank, 1), (blank, blank, 6))

    bottom_left = ((blank, 6, blank), (blank, blank, blank), (blank, blank, blank))
    bottom_center = ((blank, blank, blank), (4, 1, 9), (blank, 8, blank))
    bottom_right = ((2, 8, blank), (blank, blank, 5), (blank, 7, 9))


    left = top_left + middle_left + bottom_left
    center = top_center + middle_center + bottom_center
    right = top_right + middle_right + bottom_right
    full_grid = np.c_[left, center, right]
    return full_grid
