
total = 0

with open("text.txt") as file:
    for line in file.readlines():
        line = line.split(":")
        card = line[0]
        win_cards = line[1].split("|")[0].split()
        our_cards = line[1].split("|")[1].split()
        score = 0
        for card in our_cards:

            if card in win_cards:
                if score == 0:
                    score += 1
                else:
                    score *= 2

        total += score
print(total)
