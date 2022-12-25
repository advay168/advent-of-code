with open("./input.txt") as file:
    data = file.read().splitlines()


def SNAFU_to_DECIMAL(x: str):
    val = 0
    for char in x:
        if char == "-":
            char = -1
        elif char == "=":
            char = -2
        else:
            char = int(char)
        val *= 5
        val += char
    return val


def DECIMAL_to_SNAFU(x: int):
    val = ""
    while x > 0:
        m = x % 5
        if m == 3:
            m = -2
            val += "="
        elif m == 4:
            m = -1
            val += "-"
        else:
            val += str(m)
        x -= m
        x //= 5
    return val[::-1]


s = 0
for line in data:
    s += SNAFU_to_DECIMAL(line)
print(DECIMAL_to_SNAFU(s))
