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

    for move, clicks in moves:
        if move == "R":
            pos += clicks
        else:
            pos -= clicks
        pos = pos % 100
        if pos == 0:
            res += 1
    return res


if __name__ == "__main__":
    check_result(main(e1), 3)
    check_result(main())
