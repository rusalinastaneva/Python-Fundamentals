n = int(input())
capacity = 255
liters_in_tank = 0

for i in range(n):
    qty = int(input())

    if liters_in_tank + qty <= capacity:
        liters_in_tank += qty
    else:
        print("Insufficient capacity!")

print(liters_in_tank)