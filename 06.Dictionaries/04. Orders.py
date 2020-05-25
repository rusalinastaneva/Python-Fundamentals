prices = {}
quantities = {}

line = input()

def validate_key_existence(dictionary, key, default_value = 0):
    if key not in dictionary:
        dictionary[key] = default_value

while line != "buy":
    args = line.split()
    product = args[0]
    price = float(args[1])
    qty = int(args[2])

    validate_key_existence(quantities, product)
    quantities[product] += qty
    if product in prices:
        prices[product] = price
    else:
        prices[product] = price
    line = input()

for product, qty in quantities.items():
    print(f'{product} -> {qty * prices[product]:.2f}')
