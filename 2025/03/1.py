from utils.display import check_result
from utils.loading import read_data

e1 = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


def main(data=None):
    res = 0
    for bank in read_data(data):
        js = list(map(int, bank))
        d1 = max(js[:-1])
        d1_idx = js.index(d1)
        d2 = max(js[d1_idx + 1 :])
        res += d1 * 10 + d2
    return res


if __name__ == "__main__":
    check_result(main(e1), 357)
    check_result(main())
