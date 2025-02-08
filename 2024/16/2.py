import heapq

from utils.display import print_result
from utils.loading import read_data, RUNNING_EXAMPLE

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


def main():
    if RUNNING_EXAMPLE:
        true_min_score = 7036
    else:
        true_min_score = 135536

    grid = []
    for line in read_data(e1):
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

    queue = [(0, (cy, cx), dir, {(cy, cx)})]  # score, position, direction, track
    full_track = set()
    position_scores = {}

    while queue:
        score, (cy, cx), (cdy, cdx), track = heapq.heappop(queue)

        if score > true_min_score:
            continue

        key = (cy, cx, cdy, cdx)
        if key in position_scores and position_scores[key] < score:
            continue
        position_scores[key] = score

        if grid[cy][cx] == "E" and score == true_min_score:
            full_track.update(track)
            continue

        for dy, dx in dirs:
            ny, nx = cy + dy, cx + dx
            if grid[ny][nx] != "#":
                extra_score = 1
                if dy == cdy and dx != cdx or dy != cdy and dx == cdx:  # 180
                    extra_score += 2000
                elif dy != cdy and dx != cdx:  # 90
                    extra_score += 1000
                new_track = track | {(ny, nx)}
                heapq.heappush(
                    queue,
                    (
                        score + extra_score,
                        (ny, nx),
                        (dy, dx),
                        new_track,
                    ),
                )

    print_result(len(full_track), 45)


if __name__ == "__main__":
    main()
