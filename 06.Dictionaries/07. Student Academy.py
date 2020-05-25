stundent_count = int(input())
avg_graded_students = {}
all_students = {}

for i in range(stundent_count):
    student = input()
    grade = float(input())

    if student not in all_students:
        all_students[student] = []
    all_students[student].append(grade)

# for key, value in all_students.items():
#     avg = sum(value)/ len(value)
#     if avg >= 4.50:
#         avg_graded_students[key] = avg

avg_graded_students = {k: sum(value)/ len(value) for k, value in all_students.items() if sum(value)/len(value) >= 4.50}

avg_graded_students = dict(sorted(avg_graded_students.items(), key=lambda x: -x[1]))
[print(f'{name} -> {grade:.2f}') for name, grade in avg_graded_students.items()]