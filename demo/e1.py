input = str(input())

word = ""

#i = len(input)
# while i > 0:
#     i -= 1
#     word += (input[i])
# print(word)

for i in range(len(input)-1,-1,-1):
    word += input[i]
print(word)