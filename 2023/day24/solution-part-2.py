with open("./input.txt") as file:
    data = file.read().splitlines()

balls = []
for i, line in enumerate(data):
    pos, vel = line.split(" @ ")
    px, py, pz = map(int, pos.split(", "))
    vx, vy, vz = map(int, vel.split(", "))
    balls.append((i, (px, py, pz), (vx, vy, vz)))

def can_intersect(p0, v0, p1, v1):
    px0, py0, pz0 = p0
    vx0, vy0, vz0 = v0
    px1, py1, pz1 = p1
    vx1, vy1, vz1 = v1

    return 

for ball in balls:
    ...

print(558415252330828) # Solved manually
