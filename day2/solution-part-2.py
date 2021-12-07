with open("./input.txt") as file:
    data = [line.split(" ") for line in file.readlines()]

forward = depth = aim = 0
for direction, amount in data:
    if direction == "forward":
        forward += int(amount)
        depth += int(amount) * aim
    if direction == "down":
        aim += int(amount)
    if direction == "up":
        aim -= int(amount)
print(forward * depth)
