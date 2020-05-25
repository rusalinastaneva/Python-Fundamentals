text = input()
forces = {}
all_users = []
while text != "Lumpawaroo":
    if " | " in text:
        args = text.split(" | ")
        side = args[0]
        user = args[1]

        if side not in forces:
            forces[side] = []
        # for value_list in forces.values():
        #     for item in value_list:
        #         all_users.append(item)
        all_users = [item for value_list in forces.values() for item in value_list]
        if user not in all_users:
            forces[side].append(user)

    elif " -> " in text:
        args = text.split(" -> ")
        user = args[0]
        side = args[1]

        for key, value_list in forces.items():
            if user in value_list:
                forces[key].remove(user)
                break

        if side not in forces:
            forces[side] = []
        forces[side].append(user)
        print(f"{user} joins the {side} side!")
    text = input()

forces = dict(sorted(forces.items(), key=lambda x: (-len(x[1]), x[0])))


for key, value_list in forces.items():
    if len(value_list) == 0:
        continue

    print(f'Side: {key}, Members: {len(value_list)}')
    for value in sorted(value_list):
        print(f'! {value}')

