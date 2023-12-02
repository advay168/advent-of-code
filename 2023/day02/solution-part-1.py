with open("./input.txt") as file:
    data = file.read().splitlines()

s = 0
for line in data:
    gn, rest = line.split(":")
    gn = gn.split()[1]
    rest = rest.split("; ")
    for round in rest:
        round = round.split(", ")
        red = green = blue = 0
        for colour in round:
            n, c = colour.split()
            if c == "red":
                red = int(n)
            elif c == "green":
                green = int(n)
            elif c == "blue":
                blue = int(n)
        if red > 12 or green > 13 or blue > 14:
            break
    else:
        s += int(gn)
print(s)
