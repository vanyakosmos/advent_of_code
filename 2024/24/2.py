import re

from utils.display import check_result
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


def get_value(reg, wires, xs, ys):
    if re.match(r"x\d+", reg):
        return xs[reg]
    if re.match(r"y\d+", reg):
        return ys[reg]
    if reg in wires:
        return wires[reg]

    return None


def get_num(d, c):
    top = max(int(i[1:]) for i in d if re.match(c + r"\d+", i))
    ret = ""
    for i in range(top, -1, -1):
        try:
            ret += str(d[c + f"{i:02d}"])
        except KeyError:
            return -1
    return int(ret, 2)


def eval_loop(res, xs, ys):
    wires = {}
    while len(wires) < len(res):
        for d in res:
            op = res[d]

            v1 = get_value(op[0], wires, xs, ys)
            v2 = get_value(op[2], wires, xs, ys)

            if v1 is not None and v2 is not None:
                if op[1] == "AND":
                    wires[d] = v1 & v2
                elif op[1] == "OR":
                    wires[d] = v1 | v2
                elif op[1] == "XOR":
                    wires[d] = v1 ^ v2
    return get_num(wires, "z")


def main(data=None):
    lines = read_data(data)
    inputs_lines, ops_lines = split_lines(lines)

    xs, ys = {}, {}
    for line in inputs_lines:
        d = xs if "x" in line else ys
        ps = line.split(":")
        d[ps[0]] = int(ps[1])

    ops = {}
    rev_ops = {}
    for line in ops_lines:
        ps = line.split()
        ops[ps[4]] = (ps[0], ps[1], ps[2])
        rev_ops[(ps[0], ps[1], ps[2])] = ps[4]
        rev_ops[(ps[2], ps[1], ps[0])] = ps[4]

    top = max({int(d[1:]) for d in ops if re.match(r"z\d+", d)})

    wrong_gates = set()

    for i in range(1, top):
        x = f"x{i:02d}"
        y = f"y{i:02d}"
        z = f"z{i:02d}"

        res_op = ops[z]

        xor_gate = rev_ops[(x, "XOR", y)]
        and_gate = rev_ops[(x, "AND", y)]

        if "XOR" not in res_op:
            wrong_gates.add(z)

        carry = [
            set(o).difference({"XOR", xor_gate})
            for o in ops.values()
            if "XOR" in o and xor_gate in o
        ]
        if len(carry) != 1:
            wrong_gates.add(xor_gate)
            wrong_gates.add(and_gate)
        else:
            carry = carry[0].pop()
            xor2_gate = rev_ops[(xor_gate, "XOR", carry)]
            if xor2_gate != z:
                wrong_gates.add(xor2_gate)

    return ",".join(sorted(list(wrong_gates)))


if __name__ == "__main__":
    # check_result(main(e1))
    check_result(main())
