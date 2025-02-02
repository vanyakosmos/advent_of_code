from utils.display import print_result
from utils.loading import read_data


def main() -> None:
    lines = read_data()
    res = 0
    for y in range(len(lines) - 2):
        for x in range(len(lines[y]) - 2):
            x_mas = (
                lines[y][x]
                + lines[y][x + 2]
                + lines[y + 1][x + 1]
                + lines[y + 2][x]
                + lines[y + 2][x + 2]
            )
            if x_mas in ("MSAMS", "MMASS", "SSAMM", "SMASM"):
                res += 1
    # for line in lines:
    #     res += line.count("XMAS")
    #     res += line.count("SAMX")
    # for y in range(len(lines) - 3):
    #     for x in range(len(lines[y])):
    #         ver = lines[y][x] + lines[y + 1][x] + lines[y + 2][x] + lines[y + 3][x]
    #         if ver in ("XMAS", "SAMX"):
    #             res += 1
    # for y in range(len(lines) - 3):
    #     for x in range(len(lines[y]) - 3):
    #         diag = lines[y][x] + lines[y + 1][x + 1] + lines[y + 2][x + 2] + lines[y + 3][x + 3]
    #         if diag in ("XMAS", "SAMX"):
    #             res += 1
    #         diag = lines[y][x + 3] + lines[y + 1][x + 2] + lines[y + 2][x + 1] + lines[y + 3][x]
    #         if diag in ("XMAS", "SAMX"):
    #             res += 1
    print_result(res)


if __name__ == "__main__":
    main()
