with open("./input.txt") as file:
    data = file.read().splitlines()


def key(hand):
    js = hand.count("J")
    hand_without_j = hand.replace("J", "")
    type_ = sorted([hand_without_j.count(label) for label in set(hand_without_j)], reverse=True)
    if type_ == []:
        type_ = [0]
    type_[0] += js
    secondary = hand.translate(str.maketrans("AKQJT", "ZYX0V"))
    return type_, secondary


hands = {}
for line in data:
    hand, bid = line.split()
    hands[hand] = int(bid)

s = 0
for rank, hand in enumerate(sorted(hands, key=key), 1):
    s += rank * hands[hand]
print(s)
