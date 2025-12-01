from utils.display import check_result
from utils.loading import read_data

e1 = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def main(data=None):
    lines = read_data(data)
    moves = []
    for line in lines:
        move = line[0]
        clicks = int(line[1:])
        moves.append((move, clicks))
    res = 0
    pos = 50

    print(f"{pos}")
    for move, clicks in moves:
        if move == "R":
            new_rel_pos = pos + clicks
        else:
            new_rel_pos = pos - clicks
        new_abs_pos = new_rel_pos % 100

        inc = _cal_inc(pos, new_rel_pos)

        print(f"{pos} {move} {clicks} -> {new_rel_pos} -> {new_abs_pos} ({inc})")
        res += inc
        pos = new_abs_pos
    return res


def _cal_inc(old_pos: int, new_rel_pos: int):
    inc = 0
    if new_rel_pos < 0 < old_pos:
        inc += 1
    elif new_rel_pos == 0:
        inc += 1
    inc += abs(new_rel_pos) // 100
    return inc


if __name__ == "__main__":
    assert _cal_inc(50, -18) == 1
    assert _cal_inc(82, 52) == 0
    assert _cal_inc(52, 100) == 1
    assert _cal_inc(0, -5) == 0
    assert _cal_inc(95, 155) == 1
    assert _cal_inc(55, 0) == 1
    assert _cal_inc(0, -1) == 0
    assert _cal_inc(99, 0) == 1
    assert _cal_inc(0, 14) == 0
    assert _cal_inc(14, -68) == 1

    check_result(main(e1), 6)
    check_result(main())
