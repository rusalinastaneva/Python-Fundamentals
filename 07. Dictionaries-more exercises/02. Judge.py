command = input()
contests = {}
individual_sum_grades = {}

def validate_key_existance(dictionary, key, default_value = 0):
    if key not in dictionary:
        dictionary[key] = default_value

# contests{contest:{student:points}}
while command != "no more time":
    student = command.split(" -> ")[0]
    contest = command.split(" -> ")[1]
    points = int(command.split(" -> ")[2])

    if contest not in contests:
        contests[contest] = {student: points}
        validate_key_existance(individual_sum_grades, student)
        individual_sum_grades[student] += points

    else:
        if student in contests[contest]:
            if contests[contest][student] < points:
                contests[contest][student] = points
                validate_key_existance(individual_sum_grades, student)
                individual_sum_grades[student] = points

        else:
            contests[contest][student] = points
            validate_key_existance(individual_sum_grades, student)
            individual_sum_grades[student] += points
    command = input()

for key, inner_map in contests.items():
    print(f'{key}: {len(inner_map)} participants')
    count = 0
    inner_map = dict(sorted(inner_map.items(), key=lambda x: (-x[1], x[0])))
    for key, value in inner_map.items():
        count += 1
        print(f'{count}. {key} <::> {value}')

individual_sum_grades = dict(sorted(individual_sum_grades.items(), key=lambda x: (-x[1], x[0])))
print("Individual standings:")
count = 0
for key, value in individual_sum_grades.items():
    count += 1
    print(f'{count}. {key} -> {value}')
