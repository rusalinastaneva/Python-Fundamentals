def factorial_division(a, b):
    factorial_a = 1
    factorial_b = 1

    for i in range(0, a):
        factorial_a *= a - i
    for i in range(0, b):
        factorial_b *= b - i

    result = factorial_a/ factorial_b
    return f"{result:.2f}"

x = int(input())
y = int(input())
print(factorial_division(x, y))
