import re

from utils import print_result, read_data


def main() -> None:
    exp_re = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
    res = 0
    enabled = True
    for line in read_data(1):
        for a, b, do, dont in exp_re.findall(line):
            if do:
                enabled = True
            elif dont:
                enabled = False
            elif a and b and enabled:
                res += int(a) * int(b)
    print_result(res)


if __name__ == '__main__':
    main()
