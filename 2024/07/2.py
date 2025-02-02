import itertools

from utils.display import print_result
from utils.loading import read_data


def main() -> None:
    res = 0
    for line in read_data():
        sum_num, nums = line.split(": ")
        sum_num = int(sum_num)
        nums = [int(n) for n in nums.split(" ")]

        for combo in itertools.product("+*|", repeat=len(nums) - 1):
            val = nums[0]
            for i, sign in enumerate(combo, start=1):
                if sign == "+":
                    val += nums[i]
                elif sign == "*":
                    val *= nums[i]
                else:
                    val = int(str(val) + str(nums[i]))
            if val == sum_num:
                res += sum_num
                break

    print_result(res)


if __name__ == "__main__":
    main()
