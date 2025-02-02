DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def show_grid(grid: list[list[str]]):
    for row in grid:
        print(" ".join(row))
    print()


def iter_grid(grid: list[list]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield grid[y][x], y, x
