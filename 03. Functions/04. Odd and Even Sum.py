def sum_even_and_odd(a):
    sum_even = 0
    sum_odd = 0


    for num in str(a):
        if int(num) % 2 == 0:
            sum_even += int(num)
        else:
            sum_odd += int(num)

    print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')

n = int(input())
sum_even_and_odd(n)