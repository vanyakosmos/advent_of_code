from concurrent.futures.process import ProcessPoolExecutor
from copy import deepcopy
from heapq import heappop, heappush

from utils.display import print_result
from utils.grid import DIRS, iter_grid
from utils.loading import read_data

e1 = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""


def run(grid, cy, cx, ey, ex):
    m, n = len(grid), len(grid[0])
    queue = [(0, (cy, cx))]  # number of steps, position
    visited = set()
    while queue:
        steps, (cy, cx) = heappop(queue)

        if cy == ey and cx == ex:
            return steps

        if (cy, cx) in visited:
            continue
        visited.add((cy, cx))

        for dy, dx in DIRS:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] != "#":
                heappush(queue, (steps + 1, (ny, nx)))
    return -1


def run_on_new_grid(grid, y, x, cy, cx, ey, ex):
    print((y, x))
    new_grid = deepcopy(grid)
    new_grid[y][x] = "."
    return run(new_grid, cy, cx, ey, ex)


def main():
    # TODO
    grid = []
    for line in read_data(e1):
        grid.append(list(line))

    m, n = len(grid), len(grid[0])
    cy, cx = 0, 0
    ey, ex = 0, 0
    for e, y, x in iter_grid(grid):
        if e == "S":
            cy, cx = y, x
        elif e == "E":
            ey, ex = y, x

    res = 0
    optimal_steps = run(grid, cy, cx, ey, ex)

    with ProcessPoolExecutor() as executor:
        futures = []
        for e, y, x in iter_grid(grid):
            if 1 <= y < m - 1 and 1 <= x < n - 1 and grid[y][x] == "#":
                f = executor.submit(run_on_new_grid, grid, y, x, cy, cx, ey, ex)
                futures.append(f)
        for f in futures:
            steps = f.result()
            if optimal_steps - steps >= 100:
                res += 1

    print_result(res)


if __name__ == "__main__":
    main()
