from collections import defaultdict

from utils import read_data


def main() -> None:
    def is_mono(arr: list[int]) -> bool:
        dirs = defaultdict(list)
        for i in range(1, len(arr)):
            dirs[arr[i - 1] <= arr[i]].append(i)
        return not dirs[True] or not dirs[False]

    def is_gradual(arr: list[int]) -> bool:
        return all(1 <= abs(arr[i - 1] - arr[i]) <= 3 for i in range(1, len(arr)))

    res = 0
    for line in read_data(1):
        report = list(map(int, line.split()))
        print()
        print("REPORT :", " ".join(map(str, report)))

        i = -1
        while i < len(report):
            check_report = report.copy()
            if i >= 0:
                check_report.pop(i)
            if is_mono(check_report) and is_gradual(check_report):
                res += 1
                break
            i += 1

    print("\n\nRESULT:", res)


if __name__ == "__main__":
    main()
