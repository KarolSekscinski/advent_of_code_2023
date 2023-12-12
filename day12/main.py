
cache = {}


def count_arrangements(configuration, numbers):
    if configuration == "":
        return 1 if numbers == () else 0
    if numbers == ():
        return 0 if "#" in configuration else 1

    key = (configuration, numbers)
    if key in cache:
        return cache[key]

    result = 0
    if configuration[0] in ".?":
        result += count_arrangements(configuration[1:], numbers)

    if configuration[0] in "#?":
        if (numbers[0] <= len(configuration) and "." not in configuration[:numbers[0]] and
                (numbers[0] == len(configuration) or configuration[numbers[0]] != "#")):
            result += count_arrangements(configuration[numbers[0] + 1:], numbers[1:])
    cache[key] = result
    return result



total = 0
with open("input.txt") as file:
    for line in file.readlines():
        cfg, nums = line.split()
        cfg = "?".join([cfg] * 5)

        nums = tuple(map(int, nums.split(",")))
        nums *= 5
        # print(cfg, nums)
        total += count_arrangements(cfg, nums)
    print(total)

