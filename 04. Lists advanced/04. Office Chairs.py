n = int(input())
free_chairs = []

for i in range(1, n + 1):
    args = input().split()
    chairs = args[0]
    qty_chairs = len(chairs)
    people = int(args[1])

    if people > qty_chairs:
        print(f'{people - qty_chairs} more chairs needed in room {i}')
    else:
        free_chairs.append(qty_chairs - people)

if len(free_chairs) == n:
        print(f'Game On, {sum(free_chairs)} free chairs left')