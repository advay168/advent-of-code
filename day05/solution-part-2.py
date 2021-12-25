with open("./input.txt") as file:
    data = file.read().splitlines()
straight_lines: list[tuple[tuple[int, int], tuple[int, int]]] = []
diagonal_lines: list[tuple[tuple[int, int], tuple[int, int]]] = []


def diagonal(x1, y1, x2, y2):
    if y1 < y2:
        diagonal_lines.append(((x1, y1), (x2, y2)))
    else:
        diagonal_lines.append(((x2, y2), (x1, y1)))


def straight(x1, y1, x2, y2):
    if x1 < x2 or y1 < y2:
        straight_lines.append(((x1, y1), (x2, y2)))
    else:
        straight_lines.append(((x2, y2), (x1, y1)))


gridx, gridy = 0, 0
for line in data:
    p1, p2 = line.replace(" ", "").split("->")
    x1, y1 = p1.split(",")
    x2, y2 = p2.split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 != x2 and y1 != y2:
        diagonal(x1, y1, x2, y2)
    else:
        straight(x1, y1, x2, y2)
    gridx = max(gridx, x1, x2)
    gridy = max(gridy, y1, y2)


grid = [[0 for _ in range(gridx + 1)] for _ in range(gridy + 1)]

for (x1, y1), (x2, y2) in straight_lines:
    for i in range(0, y2 - y1 + 1):
        for j in range(0, x2 - x1 + 1):
            grid[y1 + i][x1 + j] += 1

for (x1, y1), (x2, y2) in diagonal_lines:
    for i in range(0, y2 - y1 + 1):
        j = i if x1 < x2 else -i
        grid[y1 + i][x1 + j] += 1

count = 0
for row in grid:
    for cell in row:
        if cell > 1:
            count += 1
print(count)
