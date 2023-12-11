with open("./input.txt") as file:
    data = file.read().splitlines()

import re

matches = {}
for line in data:
    g, x = line.split(":")
    _, gn = g.split()
    gn = int(gn)
    winners, mine = x.split("|")
    w = eval("{" + re.sub(" +", ",", winners.strip()) + "}")
    m = eval("{" + re.sub(" +", ",", mine.strip()) + "}")
    matches[gn] = len(w & m)

counts = {gn:1 for gn in matches}
for gn, wins in matches.items():
    for offset in range(wins):
        counts[gn + offset + 1] += counts[gn]
print(sum(counts.values()))
