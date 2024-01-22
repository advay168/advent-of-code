with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [[cell for cell in row] for row in data]

new_grid = []
for row in grid:
    if all(c == "." for c in row):
        new_grid.append(row)
    new_grid.append(row)
grid = new_grid

new_grid = []
for a, _ in enumerate(grid):
    row = []
    for i in range(len(grid[0])):
        if all(grid[j][i] == "." for j in range(len(grid))):
            row.append(grid[a][i])
        row.append(grid[a][i])
    new_grid.append(row)
grid = new_grid

galaxies = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            galaxies.append((j, i))

dists = 0
for x0, y0 in galaxies:
    for x1, y1 in galaxies:
        if (x0, y0) < (x1, y1):
            dists += abs(x1 - x0) + abs(y1 - y0)
print(dists)
