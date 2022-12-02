with open("./input.txt") as file:
    data = file.read().splitlines()


def hex_to_binary(h):
    tmp = []
    for digit in h:
        tmp.append(bin(int(digit, 16))[2:].zfill(4))
    return "".join(tmp)


def type_id(packet):
    return int(packet[3:6], 2)


def operation(t):
    if t == 0:
        return sum
    if t == 1:

        def product(lst):
            p = 1
            for x in lst:
                p *= x
            return p

        return product
    if t == 2:
        return min
    if t == 3:
        return max
    if t == 5:
        return lambda lst: int(lst[0] > lst[1])
    if t == 6:
        return lambda lst: int(lst[1] > lst[0])
    if t == 7:
        return lambda lst: int(lst[0] == lst[1])


def parse_literal_value(packet):
    lst = []
    i = 0
    while True:
        is_last, *group = packet[i * 5 : i * 5 + 5]
        lst += group
        if is_last == "0":
            break
        i += 1
    return int("".join(lst), 2), i * 5 + 5


def parse_operator(packet, op):
    inner_packets = []
    if packet[0] == "0":
        total_length = int(packet[1:16], 2)
        idx = 16
        while idx < total_length + 16:
            ti = type_id(packet[idx:])
            idx += 6
            if ti == 4:
                val, end = parse_literal_value(packet[idx:])
            else:
                val, end = parse_operator(packet[idx:], operation(ti))
            inner_packets.append(val)
            idx += end
    else:
        n_packets = int(packet[1:12], 2)
        idx = 12
        count = 0
        while count < n_packets:
            ti = type_id(packet[idx:])
            idx += 6
            if ti == 4:
                val, end = parse_literal_value(packet[idx:])
            else:
                val, end = parse_operator(packet[idx:], operation(ti))
            inner_packets.append(val)
            idx += end
            count += 1
    return op(inner_packets), idx


for line in data:
    packet = hex_to_binary(line)
    ti = type_id(packet)
    result, _ = parse_operator(packet[6:], operation(ti))
    print(result)
