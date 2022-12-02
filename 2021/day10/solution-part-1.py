with open("./input.txt") as file:
    data = file.read().splitlines()

opening_brackets = "([{<"

matching_brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}

score = {")": 3, "]": 57, "}": 1197, ">": 25137, "": 0}


def unexpected(line):
    expected = []
    for char in line:
        if char in opening_brackets:
            expected.append(matching_brackets[char])
        else:
            if char != expected.pop():
                return char
    return ""


s = 0
for line in data:
    s += score[unexpected(line)]
print(s)
