rows = int(input())
dict = {} # {String, List of strings}

for i in range(rows):
    word = input()
    synonym = input()

    if word not in dict:
        dict[word] = [] # we set its value to an empty list (since one word can have multiple synonyms)
    dict[word].append(synonym)

[print(f'{key} - {", ".join(value_list)}') for (key, value_list) in dict.items()]