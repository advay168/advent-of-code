with open("./input.txt") as file:
    data = file.read().splitlines()

grid = []
for line in data:
    grid.append([int(cell) for cell in line])

height = len(grid)
width = len(grid[-1])


def calc_score(i, j):
    val = grid[i][j]
    score = 1

    current = 1
    for x in range(j + 1, width):
        if grid[i][x] < val:
            current += 1
        else:
            break
    else:
        current -= 1
    score *= current

    current = 1
    for x in range(j - 1, -1, -1):
        if grid[i][x] < val:
            current += 1
        else:
            break
    else:
        current -= 1
    score *= current

    current = 1
    for y in range(i + 1, height):
        if grid[y][j] < val:
            current += 1
        else:
            break
    else:
        current -= 1
    score *= current

    current = 1
    for y in range(i - 1, -1, -1):
        if grid[y][j] < val:
            current += 1
        else:
            break
    else:
        current -= 1
    score *= current

    return score


m = 0
for i in range(height):
    for j in range(width):
        m = max(m, calc_score(i, j))

print(m)
