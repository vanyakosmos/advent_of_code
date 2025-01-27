from copy import deepcopy

from utils import print_result, read_data


def main() -> None:
    grid = []
    cy, cx = 0, 0
    for y, line in enumerate(read_data(1)):
        row = []
        for x, e in enumerate(line):
            if e == ".":
                row.append((0,))
            elif e == "#":
                row.append((-1,))
            elif e in ("^"):
                cy, cx = y, x
                row.append((0,))
        grid.append(row)

    m, n = len(grid), len(grid[0])

    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def show_grid():
        for y, row in enumerate(grid):
            for x, e in enumerate(row):
                v = ",".join(map(str, e))
                print(f"{v:9s}", end="")
                continue
                if e == (0,):
                    print(". ", end="")
                elif e == (-1,):
                    print("# ", end="")
                elif (y, x) == (cy, cx):
                    print("@ ", end="")
                else:
                    print("x ", end="")
            print()
        print()
        print("=" * 40)
        print()

    res = 0

    grid[cy][cx] = (1,)
    master_grid = deepcopy(grid)

    def has_loop(grid, cy, cx):
        turns = 0
        while True:
            turn_index = turns % 4 + 1
            dy, dx = dirs[turns % 4]
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < m and 0 <= nx < n):
                return False
            if -1 in grid[ny][nx]:
                turns += 1
                grid[cy][cx] += (turns % 4 + 1,)
                # show_grid()
                continue
            if 0 in grid[ny][nx]:
                grid[ny][nx] = (turn_index,)
            elif turn_index in grid[ny][nx]:
                return True
            else:  # walking pass the same spot in another direction
                grid[ny][nx] += (turn_index,)

            cy, cx = ny, nx

    for i in range(m):
        print(f"{i+1}/{m}")
        for j in range(n):
            grid = deepcopy(master_grid)
            if grid[i][j] == (0,):
                grid[i][j] = (-1,)
                if has_loop(grid, cy, cx):
                    res += 1

    print_result(res)


if __name__ == "__main__":
    main()
