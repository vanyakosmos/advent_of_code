from typing import TypeAlias

Y: TypeAlias = int
X: TypeAlias = int
Point: TypeAlias = tuple[Y, X]
DIRS: tuple[Point, ...] = ((0, 1), (1, 0), (0, -1), (-1, 0))


def read_grid(lines: list[str]):
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid


def grid_dimensions(grid: list[list]) -> tuple[Y, X]:
    return len(grid), len(grid[0])


def show_grid(grid: list[list[str]]):
    for row in grid:
        print(" ".join(row))
    print()


def iter_grid(grid: list[list]):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield grid[y][x], y, x


def is_valid_point(grid: list[list], y: int, x: int, block=None):
    m, n = len(grid), len(grid[0])
    return 0 <= y < m and 0 <= x < n and grid[y][x] != block
