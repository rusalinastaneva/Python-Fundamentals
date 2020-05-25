ciphered_skill = input()
command_line = input()

while command_line != "For Azeroth":
    command = command_line.split()[0]

    if command == "GladiatorStance":
        ciphered_skill = ciphered_skill.upper()
        print(ciphered_skill)
    elif command == "DefensiveStance":
        ciphered_skill = ciphered_skill.lower()
        print(ciphered_skill)
    elif command == "Dispel":
        index = int(command_line.split()[1])
        letter = command_line.split()[2]
        if 0 <= index <= len(ciphered_skill)-1:
            ciphered_skill = list(ciphered_skill)
            ciphered_skill[index] = letter
            ciphered_skill = ''.join(ciphered_skill)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command_line.split()[1] == "Change":
        substring1 = command_line.split()[2]
        substring2 = command_line.split()[3]
        ciphered_skill = ciphered_skill.replace(substring1, substring2)
        print(ciphered_skill)
    elif command_line.split()[1] == "Remove":
        substring = command_line.split()[2]
        ciphered_skill = ciphered_skill.replace(substring,'')
        print(ciphered_skill)
    else:
        print("Command doesn't exist!")
    command_line= input()