from collections import defaultdict
from functools import lru_cache

from utils.display import print_result
from utils.loading import read_data


def algo(n: int) -> list[int]:
    if n == 0:
        return [1]
    elif len(str(n)) % 2 == 0:
        sn = str(n)
        return [
            int(sn[: len(sn) // 2]),
            int(sn[len(sn) // 2 :]),
        ]
    else:
        return [n * 2024]


@lru_cache(maxsize=None)
def run(n, it) -> int:
    if it == 0:
        return 1
    counter = defaultdict(int)
    for next_num in algo(n):
        counter[next_num] += 1
    su = 0
    for num, count in counter.items():
        su += run(num, it - 1) * count
    return su


def main():
    line = read_data()[0]
    nums = [int(n) for n in line.split()]
    res = 0
    for n in nums:
        res += run(n, 75)
    print_result(res)


if __name__ == "__main__":
    main()
