grid = open("input.txt").read().splitlines()
# checking if there is no galaxy in row or column
empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(ch == "." for ch in col)]  # zip *grid goes column by column

galaxies = [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "#"]

total = 0
# scale = 2 part 1 scale
scale = 1000000 # part 2 scale
# finding distance between pairs of galaxies
for i, (r1, c1) in enumerate(galaxies):
    for (r2, c2) in galaxies[:i]:
        for r in range(min(r1, r2), max(r1, r2)):
            total += scale if r in empty_rows else 1
        for c in range(min(c1, c2), max(c1, c2)):
            total += scale if c in empty_cols else 1
print(total)


