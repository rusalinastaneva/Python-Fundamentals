command_line = input()
person_records = {}
while command_line != "Results":
    args = command_line.split(":")
    command = args[0]
    if command == "Add":
        person = args[1]
        health = int(args[2])
        energy = int(args[3])

        if person not in person_records:
            person_records[person] = [0, 0]
            person_records[person][0] += health
            person_records[person][1] += energy
        else:
            person_records[person][0] += health

    elif command == "Attack":
        attacker = args[1]
        defender = args[2]
        damage = int(args[3])
        if attacker and defender in person_records:
            person_records[defender][0] -= damage
            if person_records[defender][0] <= 0:
                print(f'{defender} was disqualified!')
                del person_records[defender]

            person_records[attacker][1] -= 1
            if person_records[attacker][1] <= 0:
                print(f'{attacker} was disqualified!')
                del person_records[attacker]
    elif command == "Delete":
        person = args[1]
        if person in person_records:
            del person_records[person]
        elif person == "All":
            person_records.clear()
    command_line = input()

print(f'People count: {len(person_records)}')
person_records = dict(sorted(person_records.items(), key=lambda x: (-x[1][0], x[0])))
for key, value in person_records.items():
    print(f'{key} - {value[0]} - {value[1]}')