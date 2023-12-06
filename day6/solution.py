with open("input.txt") as file:
    text = file.readlines()
    best_times = []
    # time = list(map(int, text[0].split(":")[1]))
    # distance = list(map(int, text[1].split(":")[1]))

    time = ""
    for n in text[0].split(":")[1].split():
        time += n
    time = int(time)
    distance = ""
    for n in text[1].split(":")[1].split():
        distance += n
    distance = int(distance)

    ways = 0
    for t in range(time):

        if (time - t) * t > distance:
            #print(f"You have waited for {t}, you time for travel was {time-t}, distance was {(time-t) * t}")
            ways += 1
    best_times.append(ways)
count = 1
for time in best_times:
    count *= time
print(count)