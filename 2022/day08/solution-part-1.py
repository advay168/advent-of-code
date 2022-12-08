with open("./input.txt") as file:
    data = file.read().splitlines()

grid = []
for line in data:
    grid.append([int(cell) for cell in line])

height = len(grid)
width = len(grid[-1])

visible = set()

for i in range(height):
    prev = -1
    for j in range(width):
        if grid[i][j] > prev:
            visible.add((i, j))
            prev = grid[i][j]

    prev = -1
    for j in range(width - 1, -1, -1):
        if grid[i][j] > prev:
            visible.add((i, j))
            prev = grid[i][j]

for j in range(width):
    prev = -1
    for i in range(height):
        if grid[i][j] > prev:
            visible.add((i, j))
            prev = grid[i][j]

    prev = -1
    for i in range(height - 1, -1, -1):
        if grid[i][j] > prev:
            visible.add((i, j))
            prev = grid[i][j]

print(len(visible))
