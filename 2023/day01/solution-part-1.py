with open("./input.txt") as file:
    data = file.read().splitlines()

score = 0
for line in data:
    left = 0
    for c in line:
        if c.isdigit():
            left = int(c)
            break
    right = 0
    for c in line[::-1]:
        if c.isdigit():
            right = int(c)
            break
    score += left * 10 + right

print(score)
