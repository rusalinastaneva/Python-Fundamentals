elements = input().split() # bread 10 butter 4 sugar 9 jam 12
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    bakery[key] = elements[i + 1]

searched_product = input().split()

for product in searched_product:
    if product in bakery:
        quantity = bakery[product]
        print(f'We have {quantity} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')
