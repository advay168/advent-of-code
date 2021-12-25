with open("./input.txt") as file:
    data = [line.split(" ") for line in file.readlines()]

forward = depth = 0
for direction, amount in data:
    if direction == "forward":
        forward += int(amount)
    if direction == "down":
        depth += int(amount)
    if direction == "up":
        depth -= int(amount)
print(forward * depth)
