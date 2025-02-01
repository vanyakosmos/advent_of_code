from utils import Color, print_result, read_data

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


def validate(design: str, towels: list[str]):
    if design == "":
        return True

    ok = False
    for towel in towels:
        if design.startswith(towel):
            ok = ok or validate(design[len(towel) :], towels)

    return ok


def main():
    lines = read_data(e1)
    towels = lines[0].split(", ")
    designs = lines[2:]

    res = 0
    for design in designs:
        if validate(design, towels):
            print(design, Color.GREEN("valid"))
            res += 1
        else:
            print(design, Color.RED("invalid"))
    print_result(res)


if __name__ == "__main__":
    main()
