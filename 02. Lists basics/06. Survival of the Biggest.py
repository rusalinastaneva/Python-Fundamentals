num_str = input().split()
n = int(input())

nums = []
for i in num_str:
    nums.append(int(i))

for j in range(1,n+1):
    nums.remove(min(nums))

print(nums)
