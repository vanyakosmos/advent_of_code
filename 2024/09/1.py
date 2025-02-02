from utils.display import print_result
from utils.loading import read_data


def main():
    line = read_data()[0]

    strip = []
    for i, v in enumerate(line):
        v = int(v)
        if i % 2 == 0:
            index = i - i // 2
            strip += [index] * v
        else:
            strip += [None] * v

    i, j = 0, len(strip) - 1
    while i < j:
        if strip[i] is None and strip[j] is not None:
            strip[i] = strip[j]
            strip[j] = None
            j -= 1
            i += 1
        elif strip[i] is None and strip[j] is None:
            j -= 1
        elif strip[i] is not None and strip[j] is not None:
            i += 1
        else:
            j -= 1
            i += 1

    res = 0
    for i, v in enumerate(strip):
        if v is None:
            break
        res += i * v

    print_result(res)


if __name__ == "__main__":
    main()
