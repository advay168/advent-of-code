with open("./input.txt") as file:
    data = file.read().splitlines()
lines: list[tuple[tuple[int, int], tuple[int, int]]] = []
gridx, gridy = 0, 0
for line in data:
    p1, p2 = line.replace(" ", "").split("->")
    x1, y1 = p1.split(",")
    x2, y2 = p2.split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 != x2 and y1 != y2:
        continue
    if x1 < x2 or y1 < y2:
        lines.append(((x1, y1), (x2, y2)))
    else:
        lines.append(((x2, y2), (x1, y1)))
    gridx = max(gridx, x1, x2)
    gridy = max(gridy, y1, y2)

grid = [[0 for _ in range(gridx + 1)] for _ in range(gridy + 1)]

for (x1, y1), (x2, y2) in lines:
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            grid[i][j] += 1
count = 0
for row in grid:
    for cell in row:
        if cell > 1:
            count += 1
print(count)
