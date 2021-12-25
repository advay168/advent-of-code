with open("./input.txt") as file:
    data = file.read().splitlines()
grid = []
for line in data:
    grid.append(list(line))

height = len(grid)
width = len(grid[0])


def east_of(i, j):
    return i, (j + 1) % width


def south_of(i, j):
    return (i + 1) % height, j


def move(i, j, pos_i, pos_j):
    def func(grid, char):
        grid[pos_i][pos_j] = char
        grid[i][j] = "."

    return func


def step(grid):
    changed = False
    for char, dir_func in [(">", east_of), ("v", south_of)]:
        moves = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell != char:
                    continue
                pos_i, pos_j = dir_func(i, j)
                if grid[pos_i][pos_j] != ".":
                    continue

                moves.append(move(i, j, pos_i, pos_j))
        for move_ in moves:
            move_(grid, char)
            changed = True
    return changed


i = 1
while step(grid):
    i += 1
print(i)
