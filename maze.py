'''exam, she changed the ordering of how she moved in the maze and had the students draw out where it would go. '''


def search(x, y):
    if y < 0 or y > len(grid) - 1 or x < 0 or x > len(grid[0]) - 1:
        print('Out of bounds at ({}, {})'.format(x, y))
        return False

    if grid[x][y] == 2:
        print('Found at ({}, {})'.format(x, y))
        return True
    elif grid[x][y] == 1:
        print('Wall at ({}, {})'.format(x, y))
        return False
    elif grid[x][y] == 3:
        print('Already visited at ({}, {})'.format(x, y))
        return False

    print('visiting ({}, {})'.format(x, y))

    grid[x][y] = 3

    if search(x + 1, y):
        return True
    if search(x, y - 1):
        return True
    if search(x - 1, y):
        return True
    if search(x, y + 1):
        return True

    print('Turning around')
    return False


grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]
        ]

search(0, 0)
