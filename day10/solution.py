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

seen = {(sr, sc)}
q = deque([(sr, sc)])

while q:
    r, c = q.popleft()
    ch = grid[r][c]
    # going up
    if r > 0 and ch in "S|JL" and grid[r-1][c] in "|7F" and (r - 1, c) not in seen:
        seen.add((r - 1, c))
        q.append((r - 1, c))
    # going down
    if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in seen:
        seen.add((r + 1, c))
        q.append((r + 1, c))
    # going left
    if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in seen:
        seen.add((r, c - 1))
        q.append((r, c - 1))
    # going right
    if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in seen:
        seen.add((r, c + 1))
        q.append((r, c + 1))

# total length of loop / 2 is solution
print(len(seen) // 2)
# 6903 for input.txt



