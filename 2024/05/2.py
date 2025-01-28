import math
from collections import defaultdict
from functools import cmp_to_key

from utils import print_result, read_data


def main() -> None:
    lower_than_key = defaultdict(set)

    def compare(a, b):
        if a in lower_than_key[b]:
            return 1
        if b in lower_than_key[a]:
            return -1
        return 0

    def fix_pages(pages: list[str]) -> list[str]:
        return sorted(pages, key=cmp_to_key(compare))

    res = 0
    read_ordering = True
    for line in read_data(1):
        if not line:
            read_ordering = False
        elif read_ordering:
            a, b = line.split("|")
            lower_than_key[b].add(a)
        else:
            pages = line.split(",")
            if any(
                lower_than_key[page].intersection(pages[i + 1 :])
                for i, page in enumerate(pages)
            ):
                pages = fix_pages(pages)
                res += int(pages[math.floor(len(pages) / 2)])

    print_result(res)


if __name__ == "__main__":
    main()
