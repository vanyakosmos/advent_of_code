from utils.display import check_result
from utils.loading import read_data

e1 = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def main(data=None):
    res = 0
    mat = []
    for line in read_data(data):
        row = map(lambda x: int(x == "@"), line)
        mat.append(list(row))

    while True:
        mat, rolls = _count_rolls(mat)
        res += rolls
        if rolls == 0:
            break
    return res


def _count_rolls(mat: list[list[int]]):
    res = 0
    new_mat = []
    for y in range(len(mat)):
        new_row = mat[y].copy()
        new_mat.append(new_row)
        for x in range(len(mat[y])):
            if mat[y][x] == 0:
                continue

            y0, y1 = max(0, y - 1), min(len(mat) - 1, y + 1)
            x0, x1 = max(0, x - 1), min(len(mat[0]) - 1, x + 1)
            s = 0
            for dy in range(y0, y1 + 1):
                for dx in range(x0, x1 + 1):
                    s += mat[dy][dx]
            if s <= 4:
                res += 1
                new_row[x] = 0

    return new_mat, res


if __name__ == "__main__":
    check_result(main(e1), 43)
    check_result(main())
