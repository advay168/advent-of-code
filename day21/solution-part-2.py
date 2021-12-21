with open("./input.txt") as file:
    data = file.read().splitlines()
_, p1 = data[0].split("starting position: ")
_, p2 = data[1].split("starting position: ")
pos1 = int(p1)
pos2 = int(p2)

from functools import lru_cache
from itertools import product
from collections import Counter

counts = Counter(map(sum, product(*[range(1, 4)] * 3)))


@lru_cache(None)
def winnings(pos1, pos2, score1, score2, p1_turn):
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1
    win1, win2 = 0, 0
    for i, weight in counts.items():
        if p1_turn:
            newpos1 = (pos1 + i - 1) % 10 + 1
            w1, w2 = winnings(newpos1, pos2, score1 + newpos1, score2, not p1_turn)
            win1 += w1 * weight
            win2 += w2 * weight
        else:
            newpos2 = (pos2 + i - 1) % 10 + 1
            w1, w2 = winnings(pos1, newpos2, score1, score2 + newpos2, not p1_turn)
            win1 += w1 * weight
            win2 += w2 * weight
    return win1, win2


print(max(winnings(pos1, pos2, 0, 0, True)))
