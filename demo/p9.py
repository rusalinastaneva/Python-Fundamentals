budget = float(input())
price_flour = float(input())

price_eggs = 0.75 * price_flour
price_needed_milk = (1.25 * price_flour) / 4

price_cozonac = price_eggs + price_flour + price_needed_milk
qty_cozonac = 0
eggs = 0

while budget >= price_cozonac:
        qty_cozonac += 1
        eggs += 3

        if qty_cozonac % 3 == 0:
            eggs -= qty_cozonac - 2
        budget -= price_cozonac

print(f"You made {qty_cozonac} cozonacs! Now you have {eggs} eggs and {budget:.2f}BGN left.")
