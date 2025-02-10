import math
from typing import Iterator

from utils.display import check_result, print_result
from utils.loading import batched, read_data

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
            yield v
            i += 2
        elif op == 6:
            b = math.floor(a / (2 ** read_combo(val, a, b, c)))
            i += 2
        elif op == 7:
            c = math.floor(a / (2 ** read_combo(val, a, b, c)))
            i += 2


def main(data=None) -> int:
    lines = read_data(data)
    b = read_register(lines[1])
    c = read_register(lines[2])
    ins = read_instructions(lines[4])

    shift = next(
        (
            operand
            for opcode, operand in batched(ins, 2)
            if opcode == 0 and 0 <= operand <= 3
        ),
        0,
    )
    input_bits = 7 + shift
    output_cache = {a: next(run(a, b, c, ins)) for a in range(1 << input_bits)}

    def find_quine_inputs() -> Iterator[int]:
        def helper(a: int, pointer: int = 0) -> Iterator[int]:
            if pointer >= len(ins):
                yield a
                return

            for next_bits in range(1 << shift):
                next_bits_shift = input_bits + (pointer - 1) * shift
                next_a = a | (next_bits << next_bits_shift)

                inp = next_a >> (pointer * shift)
                if output_cache[inp] == ins[pointer]:
                    yield from helper(next_a, pointer + 1)

        for inp, out in output_cache.items():
            if out == ins[0]:
                yield from helper(inp, 1)

    return min(find_quine_inputs())


if __name__ == "__main__":
    check_result(main(e1), 117440)
    print_result(main())
