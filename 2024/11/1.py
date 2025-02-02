from utils.display import print_result
from utils.loading import read_data


def main():
    line = read_data()[0]
    nums = [int(n) for n in line.split()]

    for i in range(25):
        new_nums = []
        for n in nums:
            if n == 0:
                new_nums.append(1)
            elif len(str(n)) % 2 == 0:
                sn = str(n)
                new_nums.append(int(sn[: len(sn) // 2]))
                new_nums.append(int(sn[len(sn) // 2 :]))
            else:
                new_nums.append(n * 2024)
        nums = new_nums

    print_result(len(nums))


if __name__ == "__main__":
    main()
