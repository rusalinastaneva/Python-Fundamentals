needed_experience = int(input())
battles = int(input())
total_experience = 0

for i in range(1, battles + 1):
    experience = int(input())

    if i % 3 == 0:
        total_experience += 1.15 * experience
    elif i % 5 == 0:
        total_experience += 0.90 * experience
    else:
        total_experience += experience


    if total_experience >= needed_experience:
        print(f'Player successfully collected his needed experience for {i} battles.')
        break

if total_experience < needed_experience:
    shortage = needed_experience - total_experience
    print(f'Player was not able to collect the needed experience, {shortage:.2f} more needed.')