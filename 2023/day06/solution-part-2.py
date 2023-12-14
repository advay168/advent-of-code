with open("./input.txt") as file:
    data = file.read().splitlines()

times, distances = data
time = int("".join(times.split()[1:]))
record = int("".join(distances.split()[1:]))

def d(held, total):
    return (total - held) * held

count = 0
for i in range(time):
    if d(i, time) > record:
        count += 1
print(count)
