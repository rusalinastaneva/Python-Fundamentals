words = input().split()
dict = {}

for word in words:
    word_lowerCase = word.lower()
    if word_lowerCase not in dict:
        dict[word_lowerCase] = 0
    dict[word_lowerCase] += 1

print(' '.join([f'{key}' for (key, value) in dict.items() if value % 2 == 1]))