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

    last_sign = None
    sub_res = 0
    for i in range(len(lines[0])):
        num = ""
        for line in lines[:-1]:
            num += line[i]

        if num == " " * len(lines[:-1]):
            res += sub_res
            continue

        if lines[-1][i] != " ":
            last_sign = lines[-1][i]
            sub_res = 1 if last_sign == "*" else 0

        if last_sign == "*":
            sub_res *= int(num)
        else:
            sub_res += int(num)

    return res + sub_res


if __name__ == "__main__":
    check_result(main(e1), 3263827)
    check_result(main())
