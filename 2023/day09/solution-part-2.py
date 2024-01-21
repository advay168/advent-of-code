with open("./input.txt") as file:
    data = file.read().splitlines()


def predict(nums):
    diffs = [b - a for a, b in zip(nums, nums[1:])]
    first = nums[0]
    if all(x == 0 for x in diffs):
        return first
    return first - predict(diffs)


print(sum(predict([int(n) for n in line.split()]) for line in data))
