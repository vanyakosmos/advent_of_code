import zlib

from utils.display import print_result
from utils.loading import read_data


def read_vals(line: str):
    vals = line.split("=")[1]
    return list(map(int, vals.split(",")))


def make_string(robots, m, n):
    grid = tuple(["."] * n for _ in range(m))
    for (y, x), _ in robots:
        grid[y][x] = "#"
    return "".join("".join(row) for row in grid)


def main():
    # m, n = 7, 11
    m, n = 103, 101

    robots = []

    for line in read_data():
        p, v = line.split(" ")
        px, py = read_vals(p)
        vx, vy = read_vals(v)
        robots.append([(py, px), (vy, vx)])

    min_entropy = None
    res = 0

    for sec in range(1, 10_000):
        for i, (pos, vel) in enumerate(robots):
            py, px = pos
            vy, vx = vel
            robots[i][0] = ((py + vy) % m, (px + vx) % n)

        string = make_string(robots, m, n)
        entropy = len(zlib.compress(string.encode()))

        if not min_entropy or entropy < min_entropy:
            min_entropy = entropy
            res = sec

        if sec % 1000 == 1:
            print(f"sec={sec}, min: sec={res}, entropy={min_entropy}")

    print(f"min: sec={res}, entropy={min_entropy}")
    print_result(res)


if __name__ == "__main__":
    main()
