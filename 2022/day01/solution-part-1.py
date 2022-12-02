with open("./input.txt") as file:
    data = file.read().splitlines()

lst = []
current_sum = 0
for line in data:
    if line == "":
        lst.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(line)
print(max(lst))
