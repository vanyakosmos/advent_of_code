from utils.display import print_result
from utils.loading import read_data, split_lines

e1 = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""


def read_number(wires, prefix: str):
    zs = []
    for wire, num in wires.items():
        if wire.startswith(prefix):
            zs.append((wire, num))
    zs.sort(reverse=True)
    bin = "".join(str(num) for _, num in zs)
    return int(bin, 2)


def main():
    lines = read_data(e1)
    inputs_lines, ops_lines = split_lines(lines)

    wires = {}
    for line in inputs_lines:
        name, val = line.split(": ")
        wires[name] = int(val)

    ops = []
    for line in ops_lines:
        a, op, b, c = line.replace("-> ", "").split()
        ops.append((a, b, c, op))

    while ops:
        a, b, c, op = ops.pop(0)
        if a not in wires or b not in wires:
            ops.append((a, b, c, op))
            continue
        if op == "AND":
            wires[c] = wires[a] & wires[b]
        elif op == "OR":
            wires[c] = wires[a] | wires[b]
        else:
            wires[c] = wires[a] ^ wires[b]

    z = read_number(wires, "z")
    print_result(z, 2024)


if __name__ == "__main__":
    main()
