import numpy as np


def pathfinder(matrix, position, N):
    if position == (N - 1, N - 1):
        return [(N - 1, N - 1)]
    x, y = position
    if x + 1 < N and matrix[x + 1][y] == 1:
        a = pathfinder(matrix, (x + 1, y), N)
        if a is not None:
            return [(x, y)] + a

    if y + 1 < N and matrix[x][y + 1] == 1:
        b = pathfinder(matrix, (x, y + 1), N)
        if b is not None:
            return [(x, y)] + b


Matrix = [[1, 1, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 1, 0, 0, 0], [1, 1, 1, 1, 1]]

npar = np.array(Matrix)
print(npar)

print(pathfinder(Matrix, (0, 0), 5))
