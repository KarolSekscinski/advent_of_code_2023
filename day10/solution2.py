from collections import deque

grid = open("input.txt").read().strip().splitlines()

# Finding starting pos
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

loop = {(sr, sc)}
q = deque([(sr, sc)])

maybe_s = {"|", "-", "J", "L", "7", "F"}
# BFS for grid
while q:
    r, c = q.popleft()
    ch = grid[r][c]
    # going up
    if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r - 1, c) not in loop:
        loop.add((r - 1, c))
        q.append((r - 1, c))
        if ch == "S":
            maybe_s &= {"|", "J", "L"}
    # going down
    if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in loop:
        loop.add((r + 1, c))
        q.append((r + 1, c))
        if ch == "S":
            maybe_s &= {"|", "7", "F"}
    # going left
    if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in loop:
        loop.add((r, c - 1))
        q.append((r, c - 1))
        if ch == "S":
            maybe_s &= {"-", "J", "7"}
    # going right
    if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in loop:
        loop.add((r, c + 1))
        q.append((r, c + 1))
        if ch == "S":
            maybe_s &= {"-", "L", "F"}

assert len(maybe_s) == 1
(S,) = maybe_s
# Replacing S (starting position) with pipe
grid = [row.replace("S", S) for row in grid]
# Replacing pipes outside of loop with . (ground)
grid = ["".join([ch if (r, c) in loop else "." for c, ch in enumerate(row)]) for r, row in enumerate(grid)]

outside = set()

for r, row in enumerate(grid):
    within = False
    up = None
    for c, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError(f"unexpected character (horizontal: {ch}")
        if not within:
            outside.add((r, c))
# Answer to part 2
# 265
print(len(grid) * len(grid[0]) - len(outside | loop))