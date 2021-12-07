with open("./input.txt") as file:
    data = list(map(int, file.readlines()))
prev = float("inf")
count = 0
for a, b, c in zip(data, data[1:], data[2:]):
    s = a + b + c
    if s > prev:
        count += 1
    prev = s
print(count)
