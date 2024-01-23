with open("./input.txt") as file:
    data = file.read().splitlines()

def is_possible_rle(cs, rle):
    rle = rle[:]
    prev = ""
    for c in cs:
        match c:
            case "#":
                if len(rle) == 0:
                    return False
                rle[0] -= 1
            case ".":
                if prev == "#":
                    if rle[0] != 0:
                        return False
                    rle = rle[1:]
            case "?":
                return True
        prev = c
    return rle == [] or rle == [0]

def perms(report, rle, count):
    if "?" not in report:
        return 1
    idx = report.index("?")
    report[idx] = "."
    ret = 0
    if is_possible_rle(report, rle):
        ret += perms(report, rle, count)
    if count > 0:
        report[idx] = "#"
        if is_possible_rle(report, rle):
            ret += perms(report, rle, count - 1)
    report[idx] = "?"
    return ret

count = 0
for row in data:
    report, rle = row.split()
    report = list(report)
    rle = [int(n) for n in rle.split(",")]
    count += perms(report, rle, sum(rle))
print(count)
