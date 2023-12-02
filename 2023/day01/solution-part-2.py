with open("./input.txt") as file:
    data = file.read().splitlines()

WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

score = 0
for line in data:
    left = 0
    for i, c in enumerate(line):
        if c.isdigit():
            left = int(c)
            break
        for k, v in WORDS.items():
            if line[i:].startswith(k):
                left = int(v)
                break
        else:
            continue
        break
    right = 0
    for i, c in enumerate(line[::-1]):
        if c.isdigit():
            right = int(c)
            break
        for k, v in WORDS.items():
            if line[::-1][i:][::-1].endswith(k):
                right = int(v)
                break
        else:
            continue
        break
    score += left * 10 + right

print(score)
