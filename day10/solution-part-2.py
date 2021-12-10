import statistics

with open("./input.txt") as file:
    data = file.read().splitlines()

opening_brackets = "([{<"

matching_brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}

score_table = str.maketrans({")": "1", "]": "2", "}": "3", ">": "4"})


def complete(line):
    expected = []
    for char in line:
        if char in opening_brackets:
            expected.append(matching_brackets[char])
        else:
            c = expected.pop()
            if c != char:
                return False
    return "".join(reversed(expected))


def score(completed):
    return int(completed.translate(score_table), 5)


scores = []
for line in data:
    x = complete(line)
    if x:
        scores.append(score(x))
print(statistics.median(scores))
