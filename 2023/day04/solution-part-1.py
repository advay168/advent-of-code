with open("./input.txt") as file:
    data = file.read().splitlines()

import re

winnings = []
for line in data:
    _, x = line.split(":")
    winners, mine = x.split("|")
    w = eval("{" + re.sub(" +", ",", winners.strip()) + "}")
    m = eval("{" + re.sub(" +", ",", mine.strip()) + "}")
    winnings.append(len(w & m))

print(sum(2 ** (wins - 1) for wins in winnings if wins > 0))
