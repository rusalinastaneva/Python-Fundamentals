numbers = list(map(int,input().split()))
mid = int(len(numbers)/2)
left_racer = 0
right_racer = 0

for i in range(len(numbers)):
    if i < mid:
        if numbers[i] == 0:
            left_racer *= 0.8
        left_racer += numbers[i]
    elif i > mid:
        if numbers[mid - i] == 0:
            right_racer *= 0.8
        right_racer += numbers[mid - i]

if left_racer > right_racer:
    print(f'The winner is right with total time: {right_racer:.1f}')
else:
    print(f'The winner is left with total time: {left_racer:.1f}')


