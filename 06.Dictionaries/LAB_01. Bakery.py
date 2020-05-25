elements = input().split() # bread 10 butter 4 sugar 9 jam 12
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    bakery[key] = int(elements[i + 1])

print(bakery)