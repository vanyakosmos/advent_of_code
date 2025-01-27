from utils import print_result, read_data


def show_strip(strip: list):
    for v, c in strip:
        if v == -1:
            print("." * c, end="")
        else:
            print(str(v) * c, end="")
    print()


def main():
    line = read_data(1)[0]

    strip = []
    for i, v in enumerate(line):
        v = int(v)
        if i % 2 == 0:
            index = i - i // 2
            strip.append([index, v])
        else:
            strip.append([-1, v])

    # show_strip(strip)

    j = len(strip) - 1
    while j > 0:
        rv, rc = strip[j]
        if rv == -1:
            j -= 1
            continue
        for i in range(j):
            lv, lc = strip[i]
            if lv != -1:
                continue
            if lc >= rc:
                strip.pop(j)
                strip.pop(i)
                strip.insert(i, [rv, rc])
                if lc - rc > 0:
                    strip.insert(i + 1, [-1, lc - rc])
                strip.insert(j, [-1, rc])
                break
        j -= 1
        # show_strip(strip)

    res = 0
    flat_strip = []
    for v, c in strip:
        flat_strip += [v] * c
    for i, v in enumerate(flat_strip):
        if v == -1:
            continue
        res += i * v

    print_result(res)


if __name__ == "__main__":
    main()
