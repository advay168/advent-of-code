with open("./input.txt") as file:
    data = file.read().splitlines()

times, distances = data
times = [int(x) for x in times.split()[1:]]
distances = [int(x) for x in distances.split()[1:]]

def d(held, total):
    return (total - held) * held

prod = 1
for time, record in zip(times, distances):
    count = 0
    for i in range(time):
        if d(i, time) > record:
            count += 1
    prod *= count
print(prod)
