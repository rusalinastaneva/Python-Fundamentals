def repeat_str(text, count_to_repeat):
    return ''.join([text for i in range(count_to_repeat)])


n = int(input())
upper_down_rows = n - 1

for j in range(upper_down_rows + 1):
    print(repeat_str("*", j + 1) + repeat_str(" ", upper_down_rows - j))

for k in range(upper_down_rows - 1, -1, -1):
    print(repeat_str("*", k + 1) + repeat_str(" ", upper_down_rows - k))
