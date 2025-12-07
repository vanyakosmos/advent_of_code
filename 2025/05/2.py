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
        a, b = map(int, rng.split("-"))
        ranges.append((a, b))

    i, j = 0, 0
    while True:
        if i == j:
            j += 1
            continue
        if j == len(ranges):
            i += 1
            j = 0
            continue
        if i == len(ranges):
            break
        a1, b1 = ranges[i]
        a2, b2 = ranges[j]

        if a1 <= a2 <= b1 or a1 <= b2 <= b1 or a2 <= a1 <= b2 or a2 <= b1 <= b2:
            ranges.pop(max(i, j))
            ranges[min(i, j)] = (min(a1, a2), max(b1, b2))
            i, j = 0, 0
        else:
            j += 1

    for a, b in ranges:
        res += b - a + 1

    return res


if __name__ == "__main__":
    check_result(main(e1), 14)
    check_result(main())
