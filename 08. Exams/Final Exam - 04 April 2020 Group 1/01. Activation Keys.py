key = input()

command_line = input()

while command_line != "Generate":
    args = command_line.split(">>>")
    command = args[0]

    if command == "Slice":
        start_index = int(args[1])
        end_index = int(args[2])
        key = key.replace(key[start_index:end_index],"")
        print(key)
    elif command == "Flip":
        lettersize = args[1]
        start_index = int(args[2])
        end_index = int(args[3])

        if lettersize == "Upper":
            new_part = key[start_index:end_index].upper()
            key = key.replace(key[start_index:end_index],new_part)
            print(key)
        elif lettersize == "Lower":
            new_part = key[start_index:end_index].lower()
            key = key.replace(key[start_index:end_index], new_part)
            print(key)
    elif command == "Contains":
        substring = args[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print("Substring not found!")
    command_line = input()

print(f'Your activation key is: {key}')