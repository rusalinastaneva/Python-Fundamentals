str = input().split("#")
water = int(input())
effort = 0
total_fire = 0
new_list = []

for i in range(len(str)):
    tokens = str[i].split(" = ")
    value = int(tokens[1])

    if tokens[0] == 'High' and 81 <= value <= 125:
        if water >= value:
            water -= value
            effort += 0.25 * value
            total_fire += value
            new_list.append(value)

    elif tokens[0] == 'Medium' and 51 <= value <= 80:
        if water >= value:
            water -= value
            effort += 0.25 * value
            total_fire += value
            new_list.append(value)

    elif tokens[0] == 'Low' and 1 <= value <= 50:
        if water >= value:
            water -= value
            effort += 0.25 * value
            total_fire += value
            new_list.append(value)

print("Cells:")
for i in new_list:
    print(f' - {i}')
print(f'Effort: {effort:.2f}\nTotal Fire: {total_fire}')