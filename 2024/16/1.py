import heapq

from utils import print_result, read_data

e1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

e2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""


def main():
    grid = []
    for line in read_data():
        grid.append(list(line))

    m, n = len(grid), len(grid[0])

    cy, cx = 0, 0
    for y in range(m):
        for x in range(n):
            if grid[y][x] == "S":
                cy, cx = y, x
                break

    dir = (0, 1)
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    queue = [(0, (cy, cx), dir)]  # score, position, direction
    visited = set()

    res = None

    while queue:
        score, (cy, cx), (cdy, cdx) = heapq.heappop(queue)

        if grid[cy][cx] == "E" and (not res or score < res):
            res = score
            continue

        if (cy, cx) in visited:
            continue
        visited.add((cy, cx))

        for dy, dx in dirs:
            ny, nx = cy + dy, cx + dx
            if grid[ny][nx] != "#":
                extra_score = 1
                if dy == cdy and dx != cdx or dy != cdy and dx == cdx:  # 180
                    extra_score += 2000
                elif dy != cdy and dx != cdx:  # 90
                    extra_score += 1000
                heapq.heappush(queue, (score + extra_score, (ny, nx), (dy, dx)))

    print_result(res)


if __name__ == "__main__":
    main()
