# Part 2
with open("file.txt", "r") as f:
    total = 0
    data = []
    for line in f.readlines():
        item = {'red': 0, 'green': 0, 'blue': 0}
        game_id = int(line.strip().split(':')[0].split()[1])
        subgames = line.strip().split(':')[1].strip().split(';')
        correct = True
        for game in subgames:
            game = game.split(', ')
            for parts in game:
                parts = parts.split()

                item[parts[1]] = max(item[parts[1]], int(parts[0]))
        value = item['red'] * item['green'] * item['blue']
        total += value
print(total)