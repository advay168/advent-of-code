with open("./input.txt") as file:
    data = file.read().splitlines()

positions = list(map(int, data[0].split(",")))

minPos, maxPos = min(positions), max(positions)


def cost(pos):
    return sum(abs(pos - x) for x in positions)


m = 10000000000
for i in range(minPos, maxPos):
    m = min(m, cost(i))
print(m)
