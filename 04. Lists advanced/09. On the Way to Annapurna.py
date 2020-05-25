line = input()
dict_stores = {}
# dict_stores = {'PeakSports': ['Map', 'Navigation', 'Compass'], 'Groceries': ['Dried-fruit', 'Nuts', 'Nuts']...}
while line != 'END':
    args = line.split("->")
    command = args[0]
    store_key = args[1]

    if command == 'Add':
        items = args[2]
        item_list = items.split(",")
        if store_key not in dict_stores:
            dict_stores[store_key] = item_list
        else:
            for item in item_list:
                dict_stores[store_key].append(item)
    elif command == "Remove":
        if store_key in dict_stores:
            del dict_stores[store_key]
    line = input()

# sorted by the count of the items in descending order and then by key in descending order
sorted_dict = sorted(dict_stores.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)

# sorted_dict = [('PeakSports', ['Map', 'Navigation', 'Compass']), ('Pharmacy', ['Pain-killers'])]

print("Stores list:")
for key,value in sorted_dict:
    print(key)
    for val in value:
        print(f'<<{val}>>')