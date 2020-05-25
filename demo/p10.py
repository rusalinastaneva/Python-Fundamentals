quantity = int(input())
days = int(input())
price_ornam = 2
price_skirt = 5
price_garlands = 3
price_lights = 15

spirit = 0
total_cost = 0

for i in range(1, days+1):
    if i % 2 == 0:
        total_cost += quantity * price_ornam
        spirit += 5
    if i % 3 == 0:
        total_cost += quantity * (price_skirt + price_garlands)
        spirit += 13
    elif i % 5 == 0:
        total_cost += quantity * price_lights
        spirit += 17
    if i % 15 == 0:
        spirit += 30
    elif i % 10 == 0:
        spirit -= 20
        total_cost += price_lights + price_skirt + price_garlands
        if i == days:
            spirit -= 30
    elif i % 11 == 0:
        quantity += 2

print(f"Total cost: {total_cost}\nTotal spirit: {spirit}")


