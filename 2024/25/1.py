import itertools

from utils.display import print_result
from utils.loading import read_data, split_lines

e1 = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""


def main():
    lines = read_data(e1)
    schemes = list(split_lines(lines))
    sample = schemes[0]
    m, n = len(sample), len(sample[0])

    locks = []
    keys = []

    for lines in schemes:
        is_lock = False
        hs = [0] * n
        for i, line in enumerate(lines):
            if i == 0 and line == "#" * n:
                is_lock = True
            for j, e in enumerate(line):
                if e == "#":
                    hs[j] += 1
        if is_lock:
            locks.append(hs)
        else:
            keys.append(hs)

    res = 0
    for lock in locks:
        for key in keys:
            if all(h1 + h2 <= m for h1, h2 in zip(lock, key)):
                res += 1

    print_result(res, 3)


if __name__ == "__main__":
    main()
