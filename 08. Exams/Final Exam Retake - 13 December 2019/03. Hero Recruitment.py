args = input()
heroes = {}

while args != "End":
    command = args.split()[0]
    heroname = args.split()[1]
    if command == 'Enroll':
        if heroname not in heroes:
            heroes[heroname] = []
        else:
            print(f'{heroname} is already enrolled.')
    elif command == 'Learn':
        spellname = args.split()[2]
        if heroname not in heroes:
            print(f"{heroname} doesn\'t exist.")
        elif spellname in heroes[heroname]:
            print(f'{heroname} has already learnt {spellname}.')
        else:
            heroes[heroname].append(spellname)
    elif command == 'Unlearn':
        spellname = args.split()[2]
        if heroname not in heroes:
            print(f"{heroname} doesn\'t exist.")
        elif spellname not in heroes[heroname]:
            print(f'{heroname} doesn\'t know {spellname}.')
        else:
            heroes[heroname].remove(spellname)
    args = input()
heroes = dict(sorted(heroes.items(), key=lambda x: (-len(x[1]), x[0])))

print("Heroes:")
for key, value in heroes.items():
    print(f'== {key}: {", ".join(value)}')