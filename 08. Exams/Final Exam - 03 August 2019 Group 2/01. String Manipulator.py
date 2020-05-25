text = input()
command_line = input()

while command_line != "Done":
    args = command_line.split()
    command = args[0]

    if command == "Change":
        char = args[1]
        replacement = args[2]
        text = text.replace(char, replacement)
        print(text)
    elif command == "Includes":
        result = args[1] in text
        print(result)
    elif command == "End":
        string = args[1]
        result = text.endswith(string)
        print(result)
    elif command == "Uppercase":
        text = text.upper()
        print(text)
    elif command == "FindIndex":
        char = args[1]
        index = text.index(char)
        print(index)
    elif command == "Cut":
        start_index = int(args[1])
        length = int(args[2])
        text = text[start_index:start_index+length]
        print(text)
    command_line = input()