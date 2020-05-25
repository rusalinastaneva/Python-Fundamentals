from collections import defaultdict

def print_dict(dictionary, template):
    [print(template.format(k,v)) for k,v in dictionary.items()]

key_materials = {
"fragments": 0,
"motes": 0,
"shards": 0
}
junk_dict = defaultdict(int)
legendary_items = {
"fragments": "Valanyr",
"motes": "Dragonwrath",
"shards": "Shadowmourne"
}
winner = ""

while winner == "":
    line = input().split()

    for i in range(0, len(line), 2):
        qty = int(line[i])
        material = line[i + 1].lower()

        if material in key_materials:
            key_materials[material] += qty
            if key_materials[material] >= 250:
                winner = material
                break
        else:
            junk_dict[material] += qty

key_materials[winner] -= 250
winner_item = legendary_items[winner]
print(f"{winner_item} obtained!")

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk_dict = dict(sorted(junk_dict.items()))
print_dict(key_materials,"{}: {}")
print_dict(junk_dict,"{}: {}")