with open("./input.txt") as file:
    data = file.read().splitlines()

plan = []
for line in data:
    _, _, (_, _, *colour, d, _) = line.split()
    n = int("".join(colour), base=16)
    plan.append((d, n))

cx, cy = 0, 0
points = []
for op, n in plan:
    match op:
        case "0":
            cx += n
        case "1":
            cy += n
        case "2":
            cx -= n
        case "3":
            cy -= n
    points.append((cx, cy))
points.append((0, 0))

a = 0
b = 0
for (x0, y0), (x1, y1) in zip(points, points[1:] + [points[0]]):
    a += x0 * y1 - x1 * y0
    b += abs(x1 - x0) + abs(y1 - y0)
print((abs(a) + b) // 2 + 1)
