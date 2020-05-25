tanks = input().split(", ")
command_count = int(input())

for i in range(command_count):
    args = input().split(", ")
    command = args[0]

    if command == 'Add':
        tankName = args[1]
        if tankName not in tanks:
            print("Tank successfully bought")
            tanks.append(tankName)
        else:
            print("Tank is already bought")
    elif command == 'Remove':
        tankName = args[1]
        if tankName in tanks:
            print("Tank successfully sold")
            tanks.remove(tankName)
        else:
            print("Tank not found")
    elif command == 'Remove At':
        index = int(args[1])
        if index >= len(tanks):
            print("Index out of range")
        else:
            tanks.remove(tanks[index])
            print("Tank successfully sold")
    elif command == 'Insert':
        index = int(args[1])
        tankName = args[2]
        if index < len(tanks) and tankName not in tanks:
            print("Tank successfully bought")
            tanks.insert(index, tankName)
        elif index < len(tanks) and tankName in tanks:
            print("Tank is already bought")
        else:
            print("Index out of range")

print(', '.join(tanks))
