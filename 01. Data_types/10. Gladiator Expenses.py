lost_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_helmet = 0
broken_sword = 0
broken_shiled = 0
broken_armor = 0


for i in range(1, lost_count+1):
    if i % 2 == 0:
        broken_helmet += 1
    if i % 3 == 0:
        broken_sword += 1
    if i % 6 == 0:
        broken_shiled += 1
        if broken_shiled > 1:
            if broken_shiled % 2 == 0:
                broken_armor += 1

expenses = broken_helmet*helmet_price + broken_sword*sword_price + broken_shiled*shield_price + broken_armor*armor_price

print(f'Gladiator expenses: {expenses:.2f} aureus')





