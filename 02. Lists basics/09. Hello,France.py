items = input().split("|") # Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60
budget = float(input())
new_prices = []
profit = 0

for item in items:
    tokens = item.split("->")
    type_item = tokens[0]
    price = float(tokens[1])
    isvalid = False

    if budget < price:
        continue

    if type_item == 'Clothes' and price <= 50:
        isvalid = True
    elif type_item == 'Shoes' and price <= 35:
        isvalid = True
    elif type_item == 'Accessories' and price <= 20.50:
        isvalid = True

    if isvalid:
        budget -= price
        new_price = price * 1.4
        profit += new_price - price
        new_prices.append(new_price)

print(' '.join([f'{i:.2f}' for i in new_prices]))

print(f'Profit: {profit:.2f}')
new_budget = budget + sum(new_prices)

if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

