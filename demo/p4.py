string = input()
list_str = []
for i in range(len(string)):
    list_str.append(string[i] * 2)

for j in list_str:
    print(j, end="")

# Another solution
# for letter in string:
#    print(letter * 2, end="")
