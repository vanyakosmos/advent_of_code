from utils import print_result, read_data


def read_vals(line: str):
    vals = line.split("=")[1]
    return list(map(int, vals.split(",")))


def show_grid(robots, m, n):
    grid = [[0] * n for _ in range(m)]
    for (y, x), _ in robots:
        grid[y][x] += 1
    for row in grid:
        print("".join(map(lambda e: "." if e == 0 else str(e), row)))
    print()


def main():
    # inp, m, n = 0, 7, 11
    inp, m, n = 1, 103, 101

    robots = []

    for line in read_data(inp):
        p, v = line.split(" ")
        px, py = read_vals(p)
        vx, vy = read_vals(v)
        robots.append([(py, px), (vy, vx)])

    secs = 6888
    for i, (pos, vel) in enumerate(robots):
        py, px = pos
        vy, vx = vel
        robots[i][0] = ((py + vy * secs) % m, (px + vx * secs) % n)

    show_grid(robots, m, n)

    a, b, c, d = 0, 0, 0, 0
    for (y, x), _ in robots:
        top = 0 <= y < (m - 1) // 2
        bot = (m + 1) // 2 <= y < m
        left = 0 <= x < (n - 1) // 2
        right = (n + 1) // 2 <= x < n

        if top and left:
            a += 1
        elif top and right:
            b += 1
        elif bot and left:
            c += 1
        elif bot and right:
            d += 1

    print((a, b, c, d))
    print_result(a * b * c * d)


if __name__ == "__main__":
    main()
