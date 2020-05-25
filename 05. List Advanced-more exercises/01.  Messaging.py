nums = [x for x in input().split()] # 9992 562 8933

text = input()
output = ''
indexes = []

for num in nums:
    index = 0
    for i in num:
        index += int(i)
    indexes.append(index)

for idx in indexes:
    while idx >= len(text):
        idx = 1
    output += text[idx]
    text = text[:idx] + text[idx + 1:]

print(output)





