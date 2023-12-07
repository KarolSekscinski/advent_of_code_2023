# mapping letters to use alphabetic order
letter_map = {"T": "B", "J": "1", "Q": "C", "K": "D", "A": "E"}  # Jokers are the weakest individual card


def score(cards):
    counts = [cards.count(card) for card in cards]
    if 5 in counts:
        return 6  # all the same
    if 4 in counts:
        return 5  # four of a kind
    if 3 in counts:
        if 2 in counts:
            return 4  # full house
        return 3  # three of kind
    if counts.count(2) == 4:
        return 2  # two pairs
    if 2 in counts:
        return 1  # pair
    return 0  # highest card


def replacements(cards):
    if cards == "":
        return [""]
    return [
        x + y
        for x in ("23456789TQKA" if cards[0] == "J" else cards[0])  # Loop through all possible cards for joker
        for y in replacements(cards[1:])
    ]


def classify(cards):
    return max(map(score, replacements(cards)))


def strength(cards):
    return classify(cards), [letter_map.get(card, card) for card in cards]


plays = []
with open("input.txt") as file:
    for line in file.readlines():
        hand, bid = line.split()
        plays.append((hand, int(bid)))

plays.sort(key=lambda play: strength(play[0]))

print(plays)
total = 0
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid
    print(hand, bid)
print(total)

