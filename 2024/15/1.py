from utils import noop, print_result, read_data


def show_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


def main():
    grid = []

    reading_grid = True
    moves = ""
    for line in read_data(0):
        if not line:
            reading_grid = False
        elif reading_grid:
            grid.append(list(line))
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

    def move(cy, cx, dy, dx) -> bool:
        sign = grid[cy][cx]
        ny, nx = cy + dy, cx + dx
        if grid[ny][nx] == "O":
            if move(ny, nx, dy, dx):
                grid[cy][cx] = "."
                grid[ny][nx] = sign
                print("moved another box", (cy, cx), "->", (ny, nx))
                return True
        elif grid[ny][nx] == ".":
            grid[cy][cx] = "."
            grid[ny][nx] = sign
            print("free space box move", (cy, cx), "->", (ny, nx))
            return True
        return False

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
            if grid[y][x] == "O":
                res += 100 * y + x

    print_result(res)


# print = noop


if __name__ == "__main__":
    main()
