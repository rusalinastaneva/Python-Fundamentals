n = int(input())
sum_letters = 0

for i in range(n):
    letter = input()
    sum_letters += ord(letter)
print(f'The sym equals: {sum_letters}')
