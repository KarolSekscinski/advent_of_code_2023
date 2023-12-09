# this is solution for part 2
def extrapolate(array):
    if all(x == 0 for x in array):
        return 0

    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate(deltas)
    return array[0] - diff
# solution for part 1 needed ^ return array[-1] + diff

with open("input.txt") as file:
    total = 0
    for line in file.readlines():
        story = list(map(int, line.strip().split()))
        total += extrapolate(story)

    print(total)
