num = int(input())
heroes = {}
for i in range(num):
    hero = input().split()
    name = hero[0]
    hit_points = int(hero[1])
    mana_points = int(hero[2])

    if name not in heroes:
        heroes[name] = {"HP": hit_points, "MP": mana_points}

command_line = input()
while command_line != "End":
    args = command_line.split(" - ")
    command = args[0]
    name = args[1]

    if command == "CastSpell":
        mana_needed = int(args[2])
        spell_name = args[3]
        if heroes[name]["MP"] >= mana_needed:
            heroes[name]["MP"] -= mana_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        damage = int(args[2])
        attacker = args[3]
        heroes[name]["HP"] -= damage
        if heroes[name]["HP"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
    elif command == "Recharge":
        amount = int(args[2])
        mp = heroes[name]["MP"]
        if mp + amount > 200:
            print(f"{name} recharged for {200 - mp} MP!")
            heroes[name]["MP"] = 200
        else:
            heroes[name]["MP"] += amount
            print(f"{name} recharged for {amount} MP!")
    elif command == "Heal":
        amount = int(args[2])
        hp = heroes[name]["HP"]
        if hp + amount > 100:
            print(f"{name} healed for {100 - hp} HP!")
            heroes[name]["HP"] = 100
        else:
            heroes[name]["HP"] += amount
            print(f"{name} healed for {amount} HP!")
    command_line = input()

heroes = dict(sorted(heroes.items(),key=lambda x: (-x[1]['HP'], x[0])))
for key, value in heroes.items():
    print(key)
    print(f'  HP: {value["HP"]}')
    print(f'  MP: {value["MP"]}')