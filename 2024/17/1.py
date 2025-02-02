import math

from utils.display import print_result
from utils.loading import read_data

e1 = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


def read_register(line):
    return int(line.split(": ")[1])


def read_instructions(line):
    vals = line.split(": ")[1].split(",")
    return [int(v) for v in vals]


def main():
    lines = read_data()
    a = read_register(lines[0])
    b = read_register(lines[1])
    c = read_register(lines[2])

    ins = read_instructions(lines[4])

    def read_combo(operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        raise ValueError(operand)

    output = []
    i = 0
    while i < len(ins):
        op, val = ins[i], ins[i + 1]

        print(f"i = {i:<10d}", end="\r")

        if op == 0:
            a = math.floor(a / (2 ** read_combo(val)))
            i += 2
        elif op == 1:
            b = b ^ val
            i += 2
        elif op == 2:
            b = read_combo(val) % 8
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
            v = read_combo(val) % 8
            output.append(str(v))
            i += 2
        elif op == 6:
            b = math.floor(a / (2 ** read_combo(val)))
            i += 2
        elif op == 7:
            c = math.floor(a / (2 ** read_combo(val)))
            i += 2

    print_result(",".join(output))


if __name__ == "__main__":
    main()
