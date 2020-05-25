import re
n = int(input())
count = 0

for i in range(n):
    registration = input()
    username_pattern = r"U\$([A-Z][a-z]{2,})U\$"
    password_pattern = r"P@\$([A-Za-z]{5,}\d+)P@\$"
    pattern = f"{username_pattern}{password_pattern}"

    match = re.match(pattern, registration)
    if match is None:
        print('Invalid username or password')
        continue
    count += 1
    print("Registration was successful")
    print(f'Username: {match[1]}, Password: {match[2]}')
print(f'Successful registrations: {count}')