import re

from utils.display import check_result
from utils.loading import read_data

e1 = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def main(data=None):
    lines = read_data(data)
    res = 0
    spaces_re = re.compile(r"\s+")

    nums = [[] for _ in range(len(spaces_re.split(lines[0].strip())))]

    for line in lines[:-1]:
        row = spaces_re.split(line.strip())
        for i, n in enumerate(row):
            nums[i].append(int(n))

    signs = spaces_re.split(lines[-1])
    for i, sign in enumerate(signs):
        if sign == "*":
            sub_res = 1
            for n in nums[i]:
                sub_res *= n
        else:
            sub_res = sum(nums[i])
        res += sub_res

    return res


if __name__ == "__main__":
    check_result(main(e1), 4277556)
    check_result(main())
