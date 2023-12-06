with open("input.txt") as file:
    inputs, *blocks = file.read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            overlapping_start = max(s, b)
            overlapping_end = min(e, b + c)
            if overlapping_start < overlapping_end:
                new.append((overlapping_start - b + a, overlapping_end - b + a))
                if overlapping_start > s:
                    seeds.append((s, overlapping_start))
                if e > overlapping_end:
                    seeds.append((overlapping_end, e))
                break
        else:
            new.append((s, e))

    seeds = new
print(min(seeds)[0])

