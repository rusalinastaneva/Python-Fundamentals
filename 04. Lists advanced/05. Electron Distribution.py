electrons = int(input())
e_list = []

while electrons:
    index = len(e_list) + 1
    max_el = 2*index**2
    if electrons <= max_el:
        max_el = electrons
    e_list.append(max_el)
    electrons -= max_el
print(e_list)