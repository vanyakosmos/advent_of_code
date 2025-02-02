import itertools
from collections import defaultdict

from utils.display import print_result
from utils.loading import read_data


def main() -> None:
    grid = []
    for line in read_data():
        grid.append(list(line))

    m, n = len(grid), len(grid[0])
    sigs = [[0] * n for _ in range(m)]
    all_ants = defaultdict(list)

    for y, row in enumerate(grid):
        for x, e in enumerate(row):
            if e != ".":
                all_ants[e].append((y, x))

    for ants in all_ants.values():
        for a, b in itertools.combinations(ants, 2):
            y1, x1 = a
            y2, x2 = b

            sigs[y1][x1] += 1
            sigs[y2][x2] += 1

            dy, dx = y2 - y1, x2 - x1
            ny, nx = y2 + dy, x2 + dx
            while 0 <= ny < m and 0 <= nx < n:
                sigs[ny][nx] += 1
                ny, nx = ny + dy, nx + dx

            dy, dx = y1 - y2, x1 - x2
            ny, nx = y1 + dy, x1 + dx
            while 0 <= ny < m and 0 <= nx < n:
                sigs[ny][nx] += 1
                ny, nx = ny + dy, nx + dx

    # for row in sigs:
    #     print(" ".join(map(lambda e: "#" if e > 0 else ".", row)))

    res = 0
    for row in sigs:
        res += sum([1 for e in row if e > 0])

    print_result(res)


if __name__ == "__main__":
    main()
