import heapq
from itertools import product

from utils.display import check_result, print_result
from utils.grid import DIRS, iter_grid, Point, read_grid
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


def find_distances(start: Point, grid: list[list[str]]):
    queue = [(0, start)]
    distances = {(start): 0}

    while queue:
        score, (cy, cx) = heapq.heappop(queue)

        if (cy, cx) in distances and distances[(cy, cx)] < score:
            continue

        for dy, dx in DIRS:
            ny, nx = cy + dy, cx + dx
            if grid[ny][nx] in ".SE":
                if (ny, nx) not in distances or distances[(ny, nx)] > score + 1:
                    distances[(ny, nx)] = score + 1
                    heapq.heappush(queue, (score + 1, (ny, nx)))

    return distances


def count_cheats(distances: dict[Point, int], min_time: int):
    cheat_size = 20
    res = 0
    for py, px in distances.keys():
        for dy, dx in product(range(-cheat_size, cheat_size + 1), repeat=2):
            if abs(dx) + abs(dy) > cheat_size:
                continue
            ny, nx = py + dy, px + dx
            if (ny, nx) in distances:
                initial_cost = distances[(py, px)] - distances[(ny, nx)]
                cheat_cost = abs(py - ny) + abs(px - nx)
                if (initial_cost - cheat_cost) >= min_time:
                    res += 1
    return res


def main(min_time: int, data=None):
    lines = read_data(data)
    start: Point = (0, 0)
    grid = read_grid(lines)
    for c, y, x in iter_grid(grid):
        if c == "S":
            start = (y, x)

    distances = find_distances(start, grid)
    return count_cheats(distances, min_time=min_time)


if __name__ == "__main__":
    check_result(main(min_time=50, data=e1), 285)
    print_result(main(min_time=100))
