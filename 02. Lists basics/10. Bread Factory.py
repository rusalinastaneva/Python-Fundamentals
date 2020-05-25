energy = 100
coins = 100
isClosed = False
all_events = input().split("|")  # rest-2|order-10|eggs-100|rest-10

for event in all_events:
    tokens = event.split("-")
    value = int(tokens[1])
    name = tokens[0]

    if name == "rest":
        temp = 0
        if value + energy > 100:
            temp = 100 - energy
            energy += temp
        else:
            energy += value
            temp = value

        print(f'You gained {temp} energy.\nCurrent energy: {energy}.')

    elif name == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins - value > 0:
            coins -= value
            print(f"You bought {name}.")
        else:
            print(f'Closed! Cannot afford {name}.')
            isClosed = True
            break

if not isClosed:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
