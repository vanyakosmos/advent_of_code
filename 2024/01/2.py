from collections import defaultdict

from utils.loading import read_data


def main():
    lines = read_data()
    c1 = []
    c2 = []
    for line in lines:
        a, b = line.split("   ")
        c1.append(int(a))
        c2.append(int(b))

    stats = defaultdict(int)
    for e in c2:
        stats[e] += 1
    res = 0
    for e in c1:
        res += stats[e] * e
    print(res)


if __name__ == "__main__":
    main()
