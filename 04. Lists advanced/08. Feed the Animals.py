input_line = input() # Add:Maya:7600:WaterfallArea
animals = {}
areas = {}
while input_line != "Last Info":
    args = input_line.split(":")
    command = args[0]
    animal = args[1]
    food = int(args[2])
    area = args[3]

    if command == "Add":
        if animal not in animals:
            animals[animal] = 0
            if area not in areas:
                areas[area] = 0
            areas[area] += 1
        animals[animal] += food

    elif command == "Feed":
        if animal in animals:
            animals[animal] -= food
            if animals[animal] <= 0:
                print(f'{animal} was successfully fed')
                del animals[animal]
                areas[area] -= 1
                if areas[area] == 0:
                    del areas[area]

    input_line = input()
# animals sorted in descending order by the value and then by its name in ascending order
animals_sorted = sorted(sorted(animals.items(), key=lambda x: x[0]), key=lambda y: y[1], reverse=True) # RESULT IS A LIST
areas_sorted = sorted(areas.items(), key=lambda x: x[1], reverse=True)  # in descending order by value

print("Animals:")

for y in animals_sorted:
    print(f'{y[0]} -> {y[1]}g')

print("Areas with hungry animals:")

for y in areas_sorted:
    print(f'{y[0]} : {y[1]}')