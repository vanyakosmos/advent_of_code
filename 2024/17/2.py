import math

from utils.display import print_result
from utils.loading import read_data

e1 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


def read_register(line):
    return int(line.split(": ")[1])


def read_instructions(line):
    vals = line.split(": ")[1].split(",")
    return [int(v) for v in vals]


def read_combo(operand, a, b, c):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    raise ValueError(operand)


def run(a, b, c, ins):
    output = []
    i = 0
    while i < len(ins):
        op, val = ins[i], ins[i + 1]

        if op == 0:
            a = math.floor(a / (2 ** read_combo(val, a, b, c)))
            i += 2
        elif op == 1:
            b = b ^ val
            i += 2
        elif op == 2:
            b = read_combo(val, a, b, c) % 8
            i += 2
        elif op == 3:
            if a != 0:
                i = val
            else:
                i += 2
        elif op == 4:
            b = b ^ c
            i += 2
        elif op == 5:
            v = read_combo(val, a, b, c) % 8
            output.append(v)
            i += 2
        elif op == 6:
            b = math.floor(a / (2 ** read_combo(val, a, b, c)))
            i += 2
        elif op == 7:
            c = math.floor(a / (2 ** read_combo(val, a, b, c)))
            i += 2
    return output


def main():
    # TODO
    # brute force doesn't work
    # try reverse engineer initial instruction to construct A
    lines = read_data(e1)
    b = read_register(lines[1])
    c = read_register(lines[2])

    ins = read_instructions(lines[4])

    for a in range(0, 1000000):
        output = run(a, b, c, ins)
        if a % 100000 == 0:
            print(a, output, end="\r")
        if output == ins:
            print_result(a)
            break
    else:
        print_result("NOT FOUND")


if __name__ == "__main__":
    main()
