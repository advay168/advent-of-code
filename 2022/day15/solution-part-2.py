import re
import bisect

with open("./input.txt") as file:
    data = file.read().splitlines()


def merge_insert(column, new_range):
    new_range = tuple(sorted(new_range))
    bisect.insort(column, new_range)
    idx = 0
    prev_start, prev_end = -1, -1
    while idx < len(column):
        current_start, current_end = column[idx]
        if prev_start <= current_start <= prev_end:
            prev_end = max(prev_end, current_end)
            column[idx - 1] = (prev_start, prev_end)
            column.pop(idx)
        else:
            prev_start, prev_end = column[idx]
            idx += 1


num = r"(-?\d+)"
pattern = rf"Sensor at x={num}, y={num}: closest beacon is at x={num}, y={num}"
check = 4000000
columns = [[] for _ in range(check)]
for line in data:
    if m := re.match(pattern, line):
        sx, sy, bx, by = map(int, m.groups())
        mhd = abs(sx - bx) + abs(sy - by)
        for x in range(max(-mhd, -sx), min(mhd + 1, check - sx)):
            m = mhd - abs(x)
            merge_insert(columns[sx + x], (max(sy - m, 0), min(sy + m + 1, check)))
for idx, col in enumerate(columns):
    if len(col) > 1:
        print(idx * 4000000 + col[0][-1])
