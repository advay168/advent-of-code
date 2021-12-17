with open("./input.txt") as file:
    data = file.read().splitlines()


def x_at(initial_vel, step):
    sign = 1 if initial_vel > 0 else -1
    initial_vel = abs(initial_vel)
    step = min(step, initial_vel)
    return (initial_vel * step - (step * (step - 1)) // 2) * sign


def y_at(initial_vel, step):
    return initial_vel * step - (step * (step - 1)) // 2


def will_intersect(x_vel, y_vel, x_min, x_max, y_min, y_max):
    for step in range(400):
        if x_at(x_vel, step) > x_max:
            return False
        if x_min <= x_at(x_vel, step) <= x_max and y_min <= y_at(y_vel, step) <= y_max:
            return True
    return False


x_range, y_range = data[0].removeprefix("target area: ").split(", ")
x_min, x_max = map(int, x_range[2:].split(".."))
y_min, y_max = map(int, y_range[2:].split(".."))

count = 0
for x in range(x_max + 1):
    for y in range(y_min, abs(y_min) + 1):
        if will_intersect(x, y, x_min, x_max, y_min, y_max):
            count += 1
print(count)
