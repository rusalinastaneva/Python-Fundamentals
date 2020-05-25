line = input()
dict = {}

while line != "END":
    args = line.split("->")
    command = args[0]
    road = args[1]

    if command == "Add":
        racer = args[2]
        if road not in dict:
            dict[road] = []
            dict[road].append(racer)
        else:
            if racer not in dict[road]:
                dict[road].append(racer)
    elif command == "Move":
        racer = args[2]
        next_road = args[3]

        if racer in dict[road]:
            dict[next_road].append(racer)
            dict[road].remove(racer)

    elif command == "Close":
        if road in dict:
            del dict[road]
    line = input()

# sort by the count of the VALUE LIST in DESCENDING order, then by KEY in ASCENDING order
#sorted_dist_as_list = sorted(dict.items(), key=lambda kv:(-len(kv[1]),kv[0]))
sorted_dist_as_list = sorted(sorted(dict.items(), key=lambda x: x[0]), key=lambda y: len(y[1]), reverse=True)

print('Practice sessions:')
for road, racers in sorted_dist_as_list:
    print(road)
    for value in racers:
        print(f'++{value}')