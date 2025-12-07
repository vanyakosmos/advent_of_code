from utils.display import check_result
from utils.loading import read_data, split_lines

e1 = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def main(data=None):
    lines = read_data(data)
    ranges_txt, ids_txt = split_lines(lines)
    res = 0

    ranges = []
    for rng in ranges_txt:
        ranges.append(tuple(map(int, rng.split("-"))))

    for id in ids_txt:
        id = int(id)
        for rng in ranges:
            if rng[0] <= id <= rng[1]:
                res += 1
                break
    return res


if __name__ == "__main__":
    check_result(main(e1), 3)
    check_result(main())
