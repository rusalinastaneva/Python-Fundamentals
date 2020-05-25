# Simple method using ternary operator
a, b = 20, 50
result = "B is greater than A" if a < b else "A is greater than B"
print(result)

# Method using ternary operator by tuples
c = 99
d = -50
print((d, c)[c < d])  # If c is smaller than d, print c, else print d

# Method using ternary operator by dictionary
x, y = 5, 20
print({True: x, False: y}[x < y])

# Nested if-else using ternary operator
z, m = 55, 55

print("Both are equal" if z == m else "z is greater than m" if z > m else "m is greater than z")