# Part 1
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
                item[parts[1]] = int(parts[0])
            if item['red'] > 12 or item['green'] > 13 or item['blue'] > 14:
                correct = False
                break
        if correct:
            print(game_id)
            total += game_id
print(total)




