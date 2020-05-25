def sum_numbers(a, b):
    sum = a + b
    return sum

def subtract(first_num, second_num):
    return first_num - second_num

def add_and_subtract(a, b, c):
    sum = sum_numbers(a, b)
    result = subtract(sum, c)
    return result

a = int(input())
b = int(input())
c = int(input())
res = add_and_subtract(a, b, c)
print(res)