num = 57
digits = num
sum_digits = 0

while digits > 0:
    sum_digits += digits % 10
    digits = int(digits/10)