email = input()
command = input()

while command != "Complete":
    if command == "Make Upper":
        email = email.upper()
        print(email)
    elif command == "Make Lower":
        email = email.lower()
        print(email)
    elif command.split()[0] == "GetDomain":
        count = int(command.split()[1])
        print(email[-count:])
    elif command == "GetUsername":
        if "@" in email:
            index = email.index("@")
            print(email[:index])
        else:
            print(f'The email {email} doesn\'t contain the @ symbol.')
    elif command.split()[0] == "Replace":
        char = command.split()[1]
        print(email.replace(char, "-"))
    elif command == "Encrypt":
        for ch in email:
            ascii_code = ord(ch)
            print("".join(str(ascii_code)), end=" ")
    command = input()