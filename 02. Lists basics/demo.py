gifts = input().split(" ")
command = input()

while command != "No Money":
    command = command.split(" ")
    if command[0] == "OutOfStock":
        if command[1] in gifts:
            gifts = [None if x == command[1] else x for x in gifts]
    elif command[0] == "Required":
        idx = int(command[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
    command = input()
result = [x for x in gifts if x != None]
print(" ".join(result))
#print(" ".join(map(str, result)))