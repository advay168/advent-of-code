with open("./input.txt") as file:
    data = file.read().splitlines()

balls = []
for i, line in enumerate(data):
    pos, vel = line.split(" @ ")
    px, py, pz = map(int, pos.split(", "))
    vx, vy, vz = map(int, vel.split(", "))
    balls.append((i, (px, py), (vx, vy)))

def intersection_point(p0, v0, p1, v1):
    px0, py0 = p0
    vx0, vy0 = v0
    px1, py1 = p1
    vx1, vy1 = v1

    dx, dy = px0 - px1, py0 - py1

    a = (vy1 / vx1 * dx - dy) / (vy0 - vx0 * vy1 / vx1)
    b = (vy0 / vx0 * -dx + dy) / (vy1 - vx1 * vy0 / vx0)

    return (px0 + a * vx0, py0 + a * vy0), a, b

count = 0
for i, (i0, p0, v0) in enumerate(balls):
    for i1, p1, v1 in balls[i + 1:]:
        try:
            (x, y), a, b = intersection_point(p0, v0, p1, v1)
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000 and 0 <= a and 0 <= b:
                count += 1
        except:
            pass
print(count)
