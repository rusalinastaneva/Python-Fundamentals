# Create a list of numbers using a list comprehension and then join them all together.

# 1ST WAY
str_list = []

for i in range(5):
    str_list.append("*")
print(''.join(str_list))

# 2ND SHORTEST and FASTEST SOLUTION
result = ''.join(["*" for i in range(5)])
print(result)


