import re

from utils.display import check_result
from utils.loading import read_data

e1 = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""


def main(data=None):
    lines = read_data(data)
    lines = "".join([line.removesuffix("\n") for line in lines])
    ranges = lines.split(",")
    res = 0

    rep_re = re.compile(r"^(\d+)\1+$")

    for rg in ranges:
        a, b = rg.split("-")
        a, b = int(a), int(b)

        for i in range(a, b + 1):
            if rep_re.match(str(i)):
                res += i

    return res


if __name__ == "__main__":
    check_result(main(e1), 4174379265)
    check_result(main())
