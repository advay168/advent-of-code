with open("./input.txt") as file:
    data = file.read().splitlines()

grid = [row for row in data]
grid = [list(l) for l in zip(*grid)]
s = 0
for row in grid:
    for i in range(1, len(row)):
        if row[i] != "O":
            continue
        while i > 0 and row[i - 1] == ".":
            row[i] = "."
            row[i - 1] = "O"
            i -= 1
    for i in range(len(row)):
        s += (row[i] == "O") * (len(row) - i)
print(s)
