coded_msg = input().split(" ")
decoded_msg = []

for word in coded_msg:
    first_letter = ""
    for ch in word:
        if ch.isdigit():
            first_letter += ch

    new_string = word.replace(first_letter, chr(int(first_letter)))
    str_list = list(new_string)
    str_list[1], str_list[-1] = str_list[-1], str_list[1]
    new_string = ''.join(str_list)
    decoded_msg.append(new_string)

print(' '.join(decoded_msg))
