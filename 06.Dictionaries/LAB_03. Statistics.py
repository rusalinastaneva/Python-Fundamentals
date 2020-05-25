products = {}
command = input()

while command != "statistics":
    args = command.split(": ")
    product = args[0]
    quantity = int(args[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity
    command = input()

print("Products in stock:")
# for key, value in products.items():
#     print(f'- {key}: {value}')
[print(f"- {key}: {value}") for (key, value) in products.items()]
print(f'Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}')