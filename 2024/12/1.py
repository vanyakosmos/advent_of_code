from collections import deque

from utils.display import print_result
from utils.loading import read_data


def explore(grid: list[list[str]], y: int, x: int, visited: set[tuple[int, int]]):
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    queue = deque([(y, x)])
    area = 0
    perimeter = 0
    while queue:
        y, x = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        area += 1
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] == grid[y][x]:
                    queue.append((ny, nx))
                else:
                    perimeter += 1
            else:
                perimeter += 1
    return area, perimeter


def main():
    grid = []
    for line in read_data():
        grid.append(list(line))

    m, n = len(grid), len(grid[0])
    visited = set()

    res = 0
    for y in range(m):
        for x in range(n):
            if (y, x) in visited:
                continue
            area, perimeter = explore(grid, y, x, visited)
            res += area * perimeter

    print_result(res)


if __name__ == "__main__":
    main()
