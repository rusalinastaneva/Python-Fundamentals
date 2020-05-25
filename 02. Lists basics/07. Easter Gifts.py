gifts = input().split(" ")
args = input()

while args != "No Money":
    args = args.split(" ")

    if args[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == args[1]:
                gifts[i] = 'None'

    elif args[0] == "Required":
        index = int(args[2])
        if 0 <= index < len(gifts):
            gifts[index] = args[1]

    elif args[0] == "JustInCase":
        gifts[-1] = args[1]

    args = input()

for gift in gifts:
    if gift != 'None':
        print(gift, end=" ")

# result = [x for x in gifts if x!= "None"]
# print(" ".join(result))
