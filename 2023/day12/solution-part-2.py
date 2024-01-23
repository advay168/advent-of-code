import re
import functools

with open("./input.txt") as file:
    data = file.read().splitlines()

@functools.cache
def solve(report, rle, current_run):
    if len(report) == 0:
        return rle == () and current_run == 0
    r, report = report[0], report[1:]
    s = 0
    if r in "#?":
        s += solve(report, rle, current_run + 1)
    if r in ".?" and (current_run == 0 or rle and rle[0] == current_run):
        if current_run > 0:
            rle = rle[1:]
        s += solve(report, rle, 0)
    return s

def expand(report, rle):
    n = 5
    return "?".join([report] * n) + ".", tuple(rle * n)

count = 0
for i, row in enumerate(data):
    report, rle = row.split()
    rle = [int(n) for n in rle.split(",")]
    report, rle = expand(report, rle)
    report = re.sub(r"\.+", ".", report)
    count += solve(report, rle, 0)
print(count)
