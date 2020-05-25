#1st SOLUTION
MIN_CRITERIA = 1
MAX_CRITERIA = 100
while True: # Infinite while loop
    number = float(input("Please enter a number between 1 and 100: "))
    if MIN_CRITERIA <= number <= MAX_CRITERIA:
        break
print(f'The number {number} is between 1 and 100')


#SECOND SOLUTION
# MIN_CRITERIA = 1
# MAX_CRITERIA = 100
# number = float(input())
#
# while not MIN_CRITERIA <= number <= MAX_CRITERIA:
#     number = float(input())
#
# print(f'The number {number} is between 1 and 100')