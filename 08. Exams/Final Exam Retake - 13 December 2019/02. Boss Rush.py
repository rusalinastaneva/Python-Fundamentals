import re
n = int(input())

for i in range(n):
    text = input()
    pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"
    match = re.match(pattern, text)

    if match is None:
        print("Access denied!")
        continue

    name = match[1]
    title = match[2]

    print(f'{name}, The {title}')
    print(f'>> Strength: {len(name)}')
    print(f'>> Armour: {len(title)}')