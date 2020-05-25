message = input().split()
decoded_msg = []
decoded_word = ''
last_letter = ''
second_letter = ''

for word in message:
    first_letter = ""
    for i in word:
        if i.isdigit():
            first_letter += i
        else:
            second_letter = i
            last_letter = word[-1]
            break

    first_char = chr(int(first_letter))
    second_let_indx = word.index(second_letter)
    last_let_indx = word.index(last_letter)
    if second_let_indx == last_let_indx:
        second_letter= ''
    decoded_word = first_char + last_letter + word[second_let_indx+1:-1] + second_letter
    decoded_msg.append(decoded_word)
print(' '.join(decoded_msg))