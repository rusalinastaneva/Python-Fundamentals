command_line1 = input()
cities = {}
# Havana -> Population: 410000 citizens, Gold: 1100 kg
while command_line1 != "Sail":
    args = command_line1.split("||")
    city = args[0]
    population = int(args[1])
    gold = int(args[2])

    if city not in cities:
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command_line1 = input()

command_line2 = input()
while command_line2 != "End":
    args = command_line2.split("=>")
    command = args[0]
    city = args[1]
    if command == "Plunder":
        people = int(args[2])
        gold = int(args[3])
        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')

        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            print(f'{city} has been wiped off the map!')
            del cities[city]
    elif command == "Prosper":
        gold = int(args[2])
        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            cities[city]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {city} now has {cities[city]["gold"]} gold.')
    command_line2 = input()

print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
cities = dict(sorted(cities.items(), key=lambda y: (-y[1]['gold'], y[0])))

for key, value in cities.items():
    print(f'{key} -> Population: {value["population"]} citizens, Gold: {value["gold"]} kg')