with open("./input.txt") as file:
    data = file.read().splitlines()

commands = []
for line in data:
    if line.startswith("on"):
        x, y, z = line.removeprefix("on ").split(",")
        val = True
    else:
        x, y, z = line.removeprefix("off ").split(",")
        val = False
    x = x[2:].split("..")
    y = y[2:].split("..")
    z = z[2:].split("..")
    bounds = (*map(int, x), *map(int, y), *map(int, z))
    commands.append((bounds, val))

grid = {}
for (x_min, x_max, y_min, y_max, z_min, z_max), val in commands:
    for x in range(max(x_min, -50), min(x_max, 50) + 1):
        for y in range(max(y_min, -50), min(y_max, 50) + 1):
            for z in range(max(z_min, -50), min(z_max, 50) + 1):
                grid[(x, y, z)] = val
print(sum(grid.values()))
