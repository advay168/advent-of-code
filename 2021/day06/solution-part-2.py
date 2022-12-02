with open("./input.txt") as file:
    data = file.read().splitlines()

import functools


@functools.lru_cache(None)
def fishes_spawned(num_days):
    s = 1
    for i in range(9, num_days + 9, 7):
        s += fishes_spawned(num_days - i)
    return s


days = 256

s = 0
for timer in data[0].split(","):
    s += fishes_spawned(days - int(timer))
print(s)
