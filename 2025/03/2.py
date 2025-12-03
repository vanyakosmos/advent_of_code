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
        jolt = 0
        last_idx = 0
        for i in range(11, -1, -1):
            js_slice = js[last_idx:]
            if i != 0:
                js_slice = js_slice[:-i]
            d = max(js_slice)
            last_idx += js_slice.index(d) + 1
            jolt = jolt * 10 + d
        res += jolt
    return res


if __name__ == "__main__":
    check_result(main(e1), 3121910778619)
    check_result(main())
