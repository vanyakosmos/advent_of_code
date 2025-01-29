import math

from utils import print_result, read_data


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def is_int(v: float):
    return abs(v - int(v)) < 1e-6


def find_tokens(ax, ay, bx, by, px, py) -> int:
    m = lcm(ax, ay)
    mx = m / ax
    my = m / ay

    b = (px * mx - py * my) / (bx * mx - by * my)
    a = (px - bx * b) / ax

    if is_int(a) and is_int(b):
        return 3 * a + b
    return 0


def read_vars(line: str, sep="+"):
    x, y = line.split(": ")[1].split(", ")
    x = int(x.split(sep)[1])
    y = int(y.split(sep)[1])
    return x, y


def main():
    lines = read_data(1)
    res = 0
    for i in range(0, len(lines), 4):
        ax, ay = read_vars(lines[i])
        bx, by = read_vars(lines[i + 1])
        px, py = read_vars(lines[i + 2], sep="=")

        px += 10000000000000
        py += 10000000000000
        res += find_tokens(ax, ay, bx, by, px, py)

    print_result(int(res))


if __name__ == "__main__":
    main()
