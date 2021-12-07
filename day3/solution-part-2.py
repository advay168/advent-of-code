with open("./input.txt") as file:
    data = file.read().splitlines()


def count_at(data, i):
    return sum((line[i] == "1") * 2 - 1 for line in data) >= 0


possibles = data[:]
length = len(data[0])
for i in range(length):
    count = count_at(possibles, i)
    possibles = [string for string in possibles if int(string[i]) == count]
    if len(possibles) == 1:
        break
o2 = int(possibles[0], 2)

possibles = data[:]
for i in range(length):
    count = count_at(possibles, i)
    possibles = [string for string in possibles if int(string[i]) != count]
    if len(possibles) == 1:
        break
co2 = int(possibles[0], 2)
print(o2 * co2)
