str_nums = input().split(", ")
count = int(input())
nums = []

for num in str_nums:
    nums.append(int(num))

result_sum = [0] * count # Set default values to the list

for i in range(len(nums)):
    index = i % count
    result_sum[index] += nums[i]

print(result_sum)
