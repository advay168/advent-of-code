with open("./input.txt") as file:
    data = file.read().splitlines()

# _ a b c d e f g
# a █ █ █ █ █ █ █
# b █ █ █ █ █ █ █
# c █ █ █ █ █ █ █
# d █ █ █ █ █ █ █
# e █ █ █ █ █ █ █
# f █ █ █ █ █ █ █
# g █ █ █ █ █ █ █

mapp = [
    "abcefg" ,
    "cf" ,
    "acdeg" ,
    "acdfg" ,
    "bcdf" ,
    "abdfg" ,
    "abdefg" ,
    "acf" ,
    "abcdefg" ,
    "abcdfg" ,
    ]


def char_to_index(char):
    return ord(char) - ord("a")


def signals_to_num(letters: str):
    letters = "".join(sorted(letters))
    return mapp.index(letters)


def common(sets):
    return set.intersection(*map(set,sets))


def not_n(n):
    return set("abcdefg") - common(x for x in mapp if len(x) == n)


def solve(line):
    inp, output = line.split("|")
    signals = inp.split()
    grid = [[1 for _ in range(7)] for _ in range(7)]
    for i in [2, 3, 4, 5, 6]:
        for char in common(filter(lambda letters: len(letters) == i, signals)):
            for c in map(char_to_index, not_n(i)):
                grid[char_to_index(char)][c] = 0

    translation = {}
    for _ in range(7):
        for offset, line in enumerate(grid):
            if sum(line) == 1:
                x = line.index(1)
                translation[offset + ord("a")] = chr(x + ord("a"))
                for y in range(7):
                    grid[y][x] = 0
    string = ""
    for digit in output.split():
        string += str(signals_to_num(digit.translate(translation)))
    return int(string)


print(sum(solve(line) for line in data))
