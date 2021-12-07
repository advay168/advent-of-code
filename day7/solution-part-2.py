with open("./input.txt") as file:
    data = file.read().splitlines()

positions = list(map(int, data[0].split(",")))

minPos, maxPos = min(positions), max(positions)


def cost(pos, positions):
    sum_ = 0
    for pos_ in positions:
        a = abs(pos - pos_)
        sum_ += (a * (a + 1)) // 2
    return sum_


minimum_cost = float("inf")
for pos in range(minPos, maxPos):
    minimum_cost = min(minimum_cost, cost(pos, positions))
print(minimum_cost)
