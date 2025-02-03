import re

from utils.display import print_result
from utils.loading import read_data

e1 = """
029A
980A
179A
456A
379A
"""

res_e1 = """
MY:

v<A<AA>>^AvAA<^A>Av<<A>>^AvA^Av<A>^Av<<A>^A>AAvA^Av<A<A>>^AAAvA<^A>A
  v <<   A >>  ^ A   <   A > A  v  A   <  ^ AA > A  v <   AAA >  ^ A
         <       A       ^   A     >        ^^   A        vvv      A
                 0           2                   9                 A

REAL:

<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
  v <<   A >>  ^ A   <   A > A  v  A   <  ^ AA > A   < v  AAA >  ^ A
         <       A       ^   A     >        ^^   A        vvv      A
                 0           2                   9                 A
"""

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
numpad_moveset = {"A0": ""}
numpad_coords = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
keypad_moveset = {
    # A
    "A^": "<",
    "A<": "v<<",
    "Av": "v<",
    "A>": "v",
    # ^
    "^A": ">",
    "^<": "v<",
    "^v": "v",
    "^>": "v>",
    # <
    "<A": ">>^",
    "<^": ">^",
    "<v": ">",
    "<>": ">>",
    # v
    "vA": "^>",
    "v^": "^",
    "v<": "<",
    "v>": ">",
    # >
    ">A": "^",
    ">^": "^<",
    "><": "<<",
    ">v": "<",
}
keypad_coords = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


def type_length(
    prev: str,
    next: str,
    level=0,
):
    if level == 3:
        return 1

    if level == 0:
        coords = numpad_coords
    else:
        coords = keypad_coords

    py, px = coords[prev]
    ny, nx = coords[next]

    next_code = ""
    if py > ny:
        if px > nx:
            next_code += "<" * (px - nx)
        else:
            next_code += ">" * (nx - px)
        next_code += "^" * (py - ny)
    else:
        if px > nx:
            next_code += "<" * (px - nx)
        else:
            next_code += ">" * (nx - px)
        next_code += "v" * (ny - py)
    next_code += "A"

    length = 0
    for i, v in enumerate(next_code):
        if i == 0:
            prev = "A"
        else:
            prev = next_code[i - 1]
        length += type_length(v, prev, level + 1)

    return length


def type_numpad(code: str) -> str:
    pad_map = {
        "7": (0, 0),
        "8": (0, 1),
        "9": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "1": (2, 0),
        "2": (2, 1),
        "3": (2, 2),
        "0": (3, 1),
        "A": (3, 2),
    }
    moves = ""
    cy, cx = pad_map["A"]
    for n in code:
        ny, nx = pad_map[n]
        if cy > ny:
            if cx > nx:
                moves += "<" * (cx - nx)
            else:
                moves += ">" * (nx - cx)
            moves += "^" * (cy - ny)
        else:
            if cx > nx:
                moves += "<" * (cx - nx)
            else:
                moves += ">" * (nx - cx)
            moves += "v" * (ny - cy)
        moves += "A"
        cy, cx = ny, nx
    return moves


def type_keypad(code: str) -> str:
    pad_map = {
        "^": (0, 1),
        "A": (0, 2),
        "<": (1, 0),
        "v": (1, 1),
        ">": (1, 2),
    }
    moves = ""
    cy, cx = pad_map["A"]
    for n in code:
        ny, nx = pad_map[n]
        if cy > ny:
            if n != "<":
                moves += "^" * (cy - ny)
            if cx > nx:
                moves += "<" * (cx - nx)
            else:
                moves += ">" * (nx - cx)
            if n == "<":
                moves += "^" * (cy - ny)
        else:
            if n == "<":
                moves += "v" * (ny - cy)
            if cx > nx:
                moves += "<" * (cx - nx)
            else:
                moves += ">" * (nx - cx)
            if n != "<":
                moves += "v" * (ny - cy)
        cy, cx = ny, nx
        moves += "A"
    return moves


def code_length(moves: str) -> int:
    lines = [moves]
    moves = type_numpad(moves)
    lines.append(moves)
    moves = type_keypad(moves)
    lines.append(moves)
    moves = type_keypad(moves)
    lines.append(moves)
    display_flamegraph(lines)
    return len(moves)


def display_flamegraph(lines: list[str], gaps=()):
    if not lines:
        return
    line = lines.pop()
    if gaps:
        new_line = ""
        for e, gap in zip(line, gaps):
            new_line += " " * gap + e
    else:
        new_line = line
    print(new_line)
    gaps = []
    prev = -1
    for i, e in enumerate(new_line):
        if e == "A":
            gaps.append(i - prev - 1)
            prev = i
    display_flamegraph(lines, gaps)


def main():
    res = 0
    for code in read_data(e1):
        # if code != "379A":
        #     continue
        code_num = int(re.sub(r"\D", "", code))
        le = 0
        for i, v in enumerate(code):
            prev = "A" if i == 0 else code[i - 1]
            le += type_length(prev, v)
        print(f"code {code} min length {le}")
        res += le * code_num
        # break

    print_result(res)


if __name__ == "__main__":
    main()
