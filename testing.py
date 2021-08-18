import numpy as np
played_moves = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10])
default_cell_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(played_moves)
print(default_cell_values)

def reset():
    np.place(played_moves, played_moves < 999, 1)
reset()
print(played_moves)