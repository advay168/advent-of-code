with open("./input.txt") as file:
    data = file.read().splitlines()

snd = []
for line in data:
    a, b = line.split("|")
    snd += b.split()
print(sum(1 for x in snd if len(x) in [2,3,4,7]))
