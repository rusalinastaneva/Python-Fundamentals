def char_range(char_a, char_b):
    start = ord(char_a)
    end = ord(char_b)

    for i in range(start + 1, end):
        if i != end-1:
            print(chr(i), end=" ")
        else:
            print(chr(i))


letter_one = input()
letter_two = input()
char_range(letter_one, letter_two)
