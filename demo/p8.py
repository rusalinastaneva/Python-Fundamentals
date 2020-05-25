name_1st = input()
name_2nd = input()

for i in range(len(name_1st)):
    if name_1st[i] != name_2nd[i]:
        print(name_2nd[:i+1] + name_1st[i+1:])

