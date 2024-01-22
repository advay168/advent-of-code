with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]
w, h = len(grid[0]), len(grid)

galaxies = []
for y in range(w):
    for x in range(h):
        if grid[y][x] == "#":
            galaxies.append((x, y))

scale = 1000000
dp_rows = [0]
for x in range(0, w):
    dp_rows.append(dp_rows[-1] + (scale if all(row[x] == "." for row in grid) else 1))
dp_rows = dp_rows[1:]
dp_cols = [0]
for y in range(0, h):
    dp_cols.append(dp_cols[-1] + (scale if all(c == "." for c in grid[y]) else 1))
dp_cols = dp_cols[1:]

dists = 0
for x0, y0 in galaxies:
    for x1, y1 in galaxies:
        if (x0, y0) < (x1, y1):
            dists += dp_rows[max(x0, x1)] - dp_rows[min(x0, x1)]
            dists += dp_cols[max(y0, y1)] - dp_cols[min(y0, y1)]
print(dists)
