import math

nums = list(map(int, input().split(", "))) # 9, 10, 99, 100
max_num = max(nums)
group_count = math.ceil(max_num/10)

for group in range(1, group_count + 1):
    list_10s = [num for num in nums if (group * 10 - 10) < num <= group * 10]
    print(f'Group of {group * 10}\'s: {list_10s}')
