command_line = input()
stats = {}

while command_line != "Statistics":
    command = command_line.split("->")[0]
    username = command_line.split("->")[1]

    if command == "Add":
        if username not in stats:
            stats[username] = []
        else:
            print(f'{username} is already registered')
    elif command == "Send":
        email = command_line.split("->")[2]
        stats[username].append(email)
    elif command == "Delete":
        if username in stats:
            del stats[username]
        else:
            print(f'{username} not found!')
    command_line = input()

stats = dict(sorted(stats.items(), key=lambda x: (-len(x[1]), x[0])))

print(f'Users count: {len(stats)}')
for key, value_list in stats.items():
    print(key)
    for email in value_list:
        print(f' - {email}')