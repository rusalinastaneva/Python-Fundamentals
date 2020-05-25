import re

text = input()
pattern = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
cool_emojis = []
cool_threshold = 1

emojis = re.findall(pattern, text) # returns all matches in a List

for i in text:
    if i.isdigit():
        cool_threshold *= int(i)

for emoji in emojis:
    sign = 0
    for ch in emoji[2:-2]:
        sign += ord(ch)
    if sign > cool_threshold:
        cool_emojis.append(emoji)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')

[print(x) for x in cool_emojis]
