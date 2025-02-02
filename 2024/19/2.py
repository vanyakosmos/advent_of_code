from functools import lru_cache

from utils.display import Color, print_result
from utils.loading import read_data

e1 = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


@lru_cache(maxsize=None)
def validate(design: str, towels: tuple[str, ...]):
    if not design:
        return 1

    ok = 0
    for towel in towels:
        if design.startswith(towel):
            print(Color.YELLOW("match"), design, towel)
            variants = validate(design[len(towel) :], towels)
            ok += variants

    return ok


def main():
    lines = read_data(e1)
    towels = tuple(lines[0].split(", "))
    designs = lines[2:]

    res = 0
    for design in designs:
        if ok := validate(design, towels):
            print(design, Color.GREEN(ok))
            res += ok
        else:
            print(design, Color.RED("invalid"))
    print_result(res)


if __name__ == "__main__":
    main()
