tokens = input().split() # a b c d e f g h
count = int(input())
mid = int(len(tokens)/2)

for i in range(count):
    cards = []
    for j in range(0, mid):
        cards.append(tokens[j])
        cards.append(tokens[mid])
        mid += 1

    mid = int(len(tokens) / 2)
    tokens = cards

print(tokens)

