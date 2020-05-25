def repeat_str(text, count_to_repeat):
    str_list = []
    for i in range(count_to_repeat):
        str_list.append(text)
    return ''.join(str_list)


n = int(input())
rows = 2 * n - 1
cols = 2 * n - 1
upper_and_down_rows = n - 1

for j in range(upper_and_down_rows + 1):
    print(repeat_str(" ", upper_and_down_rows - j) + "*", end="")
    print(repeat_str(" *", j))

for k in range(upper_and_down_rows-1, -1, -1):
    print(repeat_str(" ", upper_and_down_rows - k) + "*", end="")
    print(repeat_str(" *", k))
