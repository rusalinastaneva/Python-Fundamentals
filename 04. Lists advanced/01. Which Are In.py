words = input().split(", ")
text = input()

new_list = [word for word in words if word in text]
print(new_list)
# for word in words:
#         if word in text:
#             new_list.append(word)

print(new_list)