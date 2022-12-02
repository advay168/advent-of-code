with open("./input.txt") as file:
    data = file.read().splitlines()

from math import ceil


def hex_to_binary(h):
    tmp = bin(int(h, 16))[2:]
    length = ceil(len(tmp) / 4) * 4
    return tmp.zfill(length)


def version(packet):
    return int(packet[:3], 2)


def type_id(packet):
    return int(packet[3:6], 2)


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


def parse_operator(packet):
    global versions
    inner_packets = []
    if packet[0] == "0":
        total_length = int(packet[1:16], 2)
        idx = 16
        while idx < total_length + 16:
            v = version(packet[idx:])
            ti = type_id(packet[idx:])
            versions += v
            # print(packet[idx:])
            idx += 6
            if ti == 4:
                val, end = parse_literal_value(packet[idx:])
            else:
                val, end = parse_operator(packet[idx:])
            inner_packets.append(val)
            idx += end
        return inner_packets, idx
    else:
        n_packets = int(packet[1:12], 2)
        idx = 12
        count = 0
        while count < n_packets:
            v = version(packet[idx:])
            ti = type_id(packet[idx:])
            versions += v
            idx += 6
            if ti == 4:
                val, end = parse_literal_value(packet[idx:])
            else:
                val, end = parse_operator(packet[idx:])
            inner_packets.append(val)
            idx += end
            count += 1
        return inner_packets, idx


versions = 0
for line in data:
    packet = hex_to_binary(line)
    v = version(packet)
    ti = type_id(packet)
    versions += v
    if ti == 4:
        parse_literal_value(packet[6:])
    else:
        parse_operator(packet[6:])
print(versions)
