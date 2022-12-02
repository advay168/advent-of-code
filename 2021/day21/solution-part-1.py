with open("./input.txt") as file:
    data = file.read().splitlines()


def dice():
    while True:
        yield from range(1, 101)


def roll():
    return next(roll.dice)


roll.dice = dice()

_, p1 = data[0].split("starting position: ")
_, p2 = data[1].split("starting position: ")
pos1 = int(p1)
pos2 = int(p2)

score1 = 0
score2 = 0
count = 0
while True:
    pos1 += roll() + roll() + roll() - 1
    count += 3
    pos1 %= 10
    pos1 += 1
    score1 += pos1
    if score1 >= 1000:
        break
    pos2 += roll() + roll() + roll() - 1
    count += 3
    pos2 %= 10
    pos2 += 1
    if pos2 == 0:
        pos2 = 10
    score2 += pos2
    if score2 >= 1000:
        break
print(count * score2)
