with open("./input.txt") as file:
    data = list(map(int, file.readlines()))
prev = float("inf")
count = 0
for x in data:
    if x > prev:
        count += 1
    prev = x
print(count)
