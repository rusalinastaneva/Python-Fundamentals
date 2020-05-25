import re
n = int(input())

for i in range(n):
    text = input()
    pattern = r"([*@])(?P<tag>[A-Z][a-z]{2,})(\1)(: \[)(?P<one>[A-Za-z])(\]\|\[)(?P<two>[A-Za-z])(\]\|\[)(?P<three>[A-Za-z])(\]\|)$"
    match = re.search(pattern, text)

    if match is None:
        print("Valid message not found!")
        continue
    tag = match.group("tag")
    first_string = match.group("one")
    second_string = match.group("two")
    third_string = match.group("three")
    print(f'{tag}: {ord(first_string)} {ord(second_string)} {ord(third_string)}')
