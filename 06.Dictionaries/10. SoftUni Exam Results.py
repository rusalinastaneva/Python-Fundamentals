command = input()
results = {}
submissions = {}

def validate_key_existance(dictionary, key, default_value = 0):
    if key not in dictionary:
        dictionary[key] = default_value

def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))

while command != "exam finished":
    args = command.split("-")
    name = args[0]

    if args[1] == "banned":
        del results[name]
    else:
        language = args[1]
        points = int(args[2])
        validate_key_existance(results, name)
        if results[name] < points:
            results[name] = points
        validate_key_existance(submissions,language)
        submissions[language] += 1
    command = input()
results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
print_dict(results, "{} | {}")
print("Submissions:")
print_dict(submissions, "{} - {}")