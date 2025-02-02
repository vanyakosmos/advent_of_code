from utils.display import print_result, noop
from utils.loading import read_data


def show_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


def main():
    grid = []

    reading_grid = True
    moves = ""
    for line in read_data():
        if not line:
            reading_grid = False
        elif reading_grid:
            row = []
            for e in line:
                if e == "@":
                    v = "@."
                elif e == "O":
                    v = "[]"
                else:
                    v = e * 2
                row.extend(list(v))
            grid.append(row)
        else:
            moves += line

    m, n = len(grid), len(grid[0])

    cy, cx = 0, 0
    for y in range(m):
        for x in range(n):
            if grid[y][x] == "@":
                cy, cx = y, x

    dirs = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    def move_hor(cy, cx, dx):
        sign = grid[cy][cx]
        ny, nx = cy, cx + dx
        if grid[ny][nx] in "[]":
            if move_hor(ny, nx, dx):
                grid[cy][cx] = "."
                grid[ny][nx] = sign
                print("moved half of a box", (cy, cx), "->", (ny, nx))
                return True
        elif grid[ny][nx] == ".":
            grid[cy][cx] = "."
            grid[ny][nx] = sign
            print("free space box move", (cy, cx), "->", (ny, nx))
            return True
        return False

    def can_move_ver(cy, cx, dy):
        ny, nx = cy + dy, cx
        if grid[ny][nx] == ".":
            print("free space", (cy, cx), "->", (ny, nx))
            return True
        if grid[ny][nx] == "[":
            if can_move_ver(ny, nx, dy) and can_move_ver(ny, nx + 1, dy):
                print("can move from left part of a box", (cy, cx), "->", (ny, nx))
                return True
        elif grid[ny][nx] == "]":
            if can_move_ver(ny, nx - 1, dy) and can_move_ver(ny, nx, dy):
                print("can moved from right a box", (cy, cx), "->", (ny, nx))
                return True
        return False

    def move_ver(cy, cx, dy):
        sign = grid[cy][cx]
        ny, nx = cy + dy, cx
        if grid[ny][nx] == ".":
            grid[cy][cx] = "."
            grid[ny][nx] = sign
        elif grid[ny][nx] == "[":
            move_ver(ny, nx, dy)
            move_ver(ny, nx + 1, dy)
            grid[cy][cx] = "."
            grid[ny][nx] = sign
        elif grid[ny][nx] == "]":
            move_ver(ny, nx - 1, dy)
            move_ver(ny, nx, dy)
            grid[cy][cx] = "."
            grid[ny][nx] = sign

    def move(cy, cx, dy, dx) -> bool:
        if dy == 0:
            return move_hor(cy, cx, dx)
        else:
            can_move = can_move_ver(cy, cx, dy)
            print("can_move", can_move)
            if can_move:
                move_ver(cy, cx, dy)
            return can_move

    for direction in moves:
        show_grid(grid)
        print(f"direction: {direction}")
        dy, dx = dirs[direction]
        if move(cy, cx, dy, dx):
            cy, cx = cy + dy, cx + dx

    show_grid(grid)

    res = 0
    for y in range(m):
        for x in range(n):
            if grid[y][x] == "[":
                res += 100 * y + x

    print_result(res)


print = noop


if __name__ == "__main__":
    main()
