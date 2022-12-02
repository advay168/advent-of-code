with open("./input.txt") as file:
    data = file.read().splitlines()

algo = data[0]

grid = []
for line in data[2:]:
    grid.append(list(line))


def at(grid, outside, i, j):
    height = len(grid)
    width = len(grid[0])
    string = ""
    for y in [i - 1, i + 0, i + 1]:
        for x in [j - 1, j + 0, j + 1]:
            if 0 <= y < height and 0 <= x < width:
                string += grid[y][x]
            else:
                string += outside
    return algo[int(string.replace(".", "0").replace("#", "1"), 2)]


outside = "."
for _ in range(50):
    new_grid = []
    offset = 1
    for i in range(-offset, len(grid) + offset + 1):
        t = []
        for j in range(-offset, len(grid[0]) + offset + 1):
            t.append(at(grid, outside, i, j))
        new_grid.append(t)
    grid = new_grid
    outside = grid[0][0]

count = 0
for row in grid:
    for cell in row:
        count += cell == "#"
print(count)
