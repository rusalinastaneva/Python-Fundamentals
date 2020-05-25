n = int(input())
p = int(input())

courses = n // p
# 20 3 = 6
if n % p != 0:
    print(courses + 1)
else:
    print(courses)

