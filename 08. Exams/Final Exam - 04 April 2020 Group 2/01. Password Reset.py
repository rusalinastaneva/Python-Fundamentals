password = input()
command_line = input()
while command_line != "Done":
    args = command_line.split()
    command = args[0]
    if command == "TakeOdd":
        new_password = ""
        for i in range(1, len(password), 2):
            new_password += password[i]
        password = new_password
        print(password)
    elif command == "Cut":
        index = int(args[1])
        length = int(args[2])
        old_part = password[index: index + length]
        password = password.replace(old_part, "")
        print(password)
    elif command == "Substitute":
        substring = args[1]
        substitute = args[2]

        if substring not in password:
            print("Nothing to replace!")
        else:
            password = password.replace(substring, substitute)
            print(password)
    command_line = input()

print(f'Your password is: {password}')