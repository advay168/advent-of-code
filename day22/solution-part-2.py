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

from functools import cache


@cache
def status_of(commands, x_min_, x_max_, y_min_, y_max_, z_min_, z_max_):
    count = 0
    for i, ((x_min, x_max, y_min, y_max, z_min, z_max), val) in enumerate(commands):
        x_min = max(x_min, x_min_)
        x_max = min(x_max, x_max_)
        if x_min > x_max:
            continue
        y_min = max(y_min, y_min_)
        y_max = min(y_max, y_max_)
        if y_min > y_max:
            continue
        z_min = max(z_min, z_min_)
        z_max = min(z_max, z_max_)
        if z_min > z_max:
            continue
        x_diff = x_max - x_min + 1
        y_diff = y_max - y_min + 1
        z_diff = z_max - z_min + 1
        c = status_of(commands[:i], x_min, x_max, y_min, y_max, z_min, z_max)
        count -= c
        if val:
            count += x_diff * y_diff * z_diff
    return count


inf = float("inf")
print(status_of(tuple(commands), -inf, inf, -inf, inf, -inf, inf))
