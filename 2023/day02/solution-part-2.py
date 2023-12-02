with open("./input.txt") as file:
    data = file.read().splitlines()

s = 0
for line in data:
    gn, rest = line.split(":")
    gn = gn.split()[1]
    rest = rest.split("; ")
    red = green = blue = 0
    for round in rest:
        round = round.split(", ")
        for colour in round:
            n, c = colour.split()
            if c == "red":
                red = max(red, int(n))
            elif c == "green":
                green = max(green,int(n))
            elif c == "blue":
                blue = max(blue, int(n))
    s += red * green * blue
print(s)
