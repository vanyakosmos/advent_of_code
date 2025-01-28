from collections import deque

from utils import print_result, read_data


def count_sides(
    hor_sides: set[tuple[str, int, int]],
    ver_sides: set[tuple[str, int, int]],
) -> int:
    """
    ......CC..
    ......CCC.
    .....CC...
    ...CCC....
    ....C.....
    ....CC....
    .....C....
    ..........
    """

    res = 0
    hor = sorted(hor_sides, key=lambda x: (x[0], x[2], x[1]))
    for i in range(len(hor) - 1):
        d1, y1, x1 = hor[i]
        d2, y2, x2 = hor[i + 1]
        if not (d1 == d2 and x1 == x2 and y2 - y1 == 1):
            res += 1
    ver = sorted(ver_sides, key=lambda x: (x[0], x[1], x[2]))
    for i in range(len(ver) - 1):
        d1, y1, x1 = ver[i]
        d2, y2, x2 = ver[i + 1]
        if not (d1 == d2 and y1 == y2 and x2 - x1 == 1):
            res += 1
    return res + 2


def explore(grid: list[list[str]], y: int, x: int, visited: set[tuple[int, int]]):
    dirs = (("east", 0, 1), ("west", 0, -1), ("south", 1, 0), ("north", -1, 0))
    queue = deque([(y, x)])
    area = 0
    hor_sides = set()
    ver_sides = set()
    while queue:
        y, x = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        area += 1
        for direction, dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] == grid[y][x]:
                    queue.append((ny, nx))
                else:
                    sides = hor_sides if direction in ("east", "west") else ver_sides
                    sides.add((direction, y, x))
            else:
                sides = hor_sides if direction in ("east", "west") else ver_sides
                sides.add((direction, y, x))

    return area, count_sides(hor_sides, ver_sides)


def main():
    grid = []
    for line in read_data(1):
        grid.append(list(line))

    m, n = len(grid), len(grid[0])
    visited = set()

    res = 0
    for y in range(m):
        for x in range(n):
            if (y, x) in visited:
                continue
            area, sides = explore(grid, y, x, visited)
            res += area * sides

    print_result(res)


if __name__ == "__main__":
    main()
