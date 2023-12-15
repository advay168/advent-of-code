with open("./input.txt") as file:
    data = file.read().splitlines()


def key(hand):
    type_ = sorted([hand.count(label) for label in set(hand)], reverse=True)
    secondary = hand.translate(str.maketrans("AKQJT", "ZYXWV"))
    return type_, secondary


hands = {}
for line in data:
    hand, bid = line.split()
    hands[hand] = int(bid)

s = 0
for rank, hand in enumerate(sorted(hands, key=key), 1):
    s += rank * hands[hand]
print(s)
