from heapq import heappop, heappush

from utils.display import print_result
from utils.loading import read_data, RUNNING_EXAMPLE
from utils.grid import DIRS, show_grid

e1 = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""


def main():
    if RUNNING_EXAMPLE:
        m, n = 7, 7
        limit = 12
    else:
        m, n = 71, 71
        limit = 1024

    grid = [["."] * n for _ in range(m)]
    for i, line in enumerate(read_data(e1)):
        if i == limit:
            break
        x, y = map(int, line.split(","))
        grid[y][x] = "#"

    show_grid(grid)

    queue = [(0, (0, 0))]  # number of steps, position
    visited = set()

    res = 0

    while queue:
        steps, (cy, cx) = heappop(queue)

        if cy == m - 1 and cx == n - 1:
            res = steps
            break

        if (cy, cx) in visited:
            continue
        visited.add((cy, cx))

        for dy, dx in DIRS:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] != "#":
                heappush(queue, (steps + 1, (ny, nx)))

    print_result(res)


if __name__ == "__main__":
    main()
