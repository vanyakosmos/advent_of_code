from utils.display import print_result
from utils.loading import read_data

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
    # TODO
    # true_min_score = 7036
    true_min_score = 11048
    # true_min_score = 135536

    grid = []
    for line in read_data(e2):
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

    queue = [(0, set(), (cy, cx), dir)]  # score, track, position, direction
    full_track = set()
    visited = {}

    i = 0
    while queue:
        score, track, (cy, cx), (cdy, cdx) = queue.pop()

        i += 1
        if i % 100000 == 0:
            print(
                f"i={i // 100000:<5d} "
                f"queue={len(queue):<10d} "
                f"score={score:<10d} "
                f"track={len(track):<10d} "
                f"full_track={len(full_track)}",
                end="\r",
            )

        if score > true_min_score:
            continue

        if (cy, cx) in track:
            continue
        track = track | {(cy, cx)}

        # if (cy, cx) in visited and score > visited[(cy, cx)]:
        #     continue
        # visited[(cy, cx)] = score

        if grid[cy][cx] == "E":
            print(f"finish score {score}")

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
                queue.append(
                    (
                        score + extra_score,
                        track,
                        # track | {(ny, nx)},
                        (ny, nx),
                        (dy, dx),
                    )
                )
                # heapq.heappush(
                #     queue,
                #     (
                #         score + extra_score,
                #         track,
                #         (ny, nx),
                #         (dy, dx),
                #     ),
                # )

    # for y, x in full_track:
    #     grid[y][x] = Color.YELLOW("+")
    # show_grid(grid)

    print_result(len(full_track))


if __name__ == "__main__":
    main()
