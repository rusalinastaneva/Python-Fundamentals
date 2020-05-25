def perfect_number(num):
    positive_divisor = 0

    for i in range(1, num):
        if num % i == 0:
            positive_divisor += i

    if positive_divisor == num:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'

n = int(input())
result = perfect_number(n)
print(result)