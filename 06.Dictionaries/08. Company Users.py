line = input()
companies = {}

while line != "End":
    args = line.split(" -> ")
    company = args[0]
    employee_id = args[1]

    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

    line = input()

companies = dict(sorted(companies.items()))
for key, value_list in companies.items():
    print(key)
    for value in value_list:
        print(f'-- {value}')