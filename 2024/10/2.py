from collections import deque

from utils import noop, print_result, read_data


def main():
    grid = []
    for line in read_data(1):
        grid.append(list(map(int, line)))

    m, n = len(grid), len(grid[0])

    heads = []
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == 0:
                heads.append((y, x))

    res = 0
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for y, x in heads:
        queue = deque([(y, x)])
        visited = set()

        while queue:
            cy, cx = queue.popleft()
            print((cy, cx))
            for dy, dx in dirs:
                ny, nx = cy + dy, cx + dx
                print("next", (ny, nx))
                if (ny, nx) in visited:
                    continue
                if 0 <= ny < m and 0 <= nx < n:
                    print("diff", grid[ny][nx], grid[cy][cx])
                    if grid[ny][nx] - grid[cy][cx] == 1:
                        if grid[ny][nx] == 9:
                            res += 1
                        else:
                            queue.append((ny, nx))
            visited.add((cy, cx))

    print_result(res)


print = noop

if __name__ == "__main__":
    main()
