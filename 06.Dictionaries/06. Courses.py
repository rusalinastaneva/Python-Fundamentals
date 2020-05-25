commandLine = input()
courses_db = {}

while commandLine != "end":
    args = commandLine.split(" : ")
    course = args[0]
    name = args[1]

    if course not in courses_db:
        courses_db[course] = []
    courses_db[course].append(name)

    commandLine = input()

courses_db = dict(sorted(courses_db.items(), key=lambda x: len(x[1]), reverse=True))

for key, value_list in courses_db.items():
    print(f'{key}: {len(value_list)}')
    for name in sorted(value_list):
        print(f'-- {name}')