import re

with open("./input.txt") as file:
    data = file.read().splitlines()

num = r"(-?\d+)"
sensors = []
beacons = []
pattern = rf"Sensor at x={num}, y={num}: closest beacon is at x={num}, y={num}"
count = set()
check = 2000000
for line in data:
    if m := re.match(pattern, line):
        sx, sy, bx, by = map(int, m.groups())
        sensors.append((sx, sy))
        beacons.append((bx, by))
        mhd = abs(sx - bx) + abs(sy - by)
        for x in range(-mhd, mhd + 1):
            m = mhd - abs(x)
            if check - sy in range(-m, m + 1):
                count.add(sx + x)

c = 0
for coord in count:
    if (coord, check) not in beacons and (coord, check) not in sensors:
        c += 1
print(c)
