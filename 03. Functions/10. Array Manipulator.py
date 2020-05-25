# THIS SOLUTION IS NOT CORRECT - RESULT 50/100
import sys

def read_number_arr():
    nums = list(map(int, input().split(" ")))
    return nums

def exchange(nums, index):
    if 0 <= index < len(nums):
        arr = nums[index + 1:] + nums[:index + 1]
        return arr
    else:
        print("Invalid index")
        return nums

def max_even_or_odd(nums, type):
    max_num = -sys.maxsize
    result = 0
    if type == "even":
        for i in nums:
            if i % 2 == 0 and i >= max_num:
                max_num = i
                result = nums.index(max_num)
    elif type == "odd":
        for i in nums:
            if i % 2 == 1 and i >= max_num:
                max_num = i
                result = nums.index(max_num)
    return result

def min_even_or_odd(nums, type):
    min_num = sys.maxsize
    result = -1

    if type == "even":
        for i in nums:
            if i % 2 == 0 and i <= min_num:
                min_num = i
                result = nums.index(min_num)
    elif type == "odd":
        for i in nums:
            if i % 2 == 1 and i <= min_num:
                min_num = i
                result = nums.index(min_num)
    return result

def first_even_odd(nums, count, type):
    elements = []

    if type == "even":
        for num in nums:
            if num % 2 == 0 and len(elements) < count:
                elements.append(num)
    elif type == "odd":
        for num in nums:
            if num % 2 != 0 and len(elements) < count:
                elements.append(num)
    return elements

def last_even_odd(nums, count, type):
    elements = []
    if type == "even":
        for i in range(len(nums)-1,-1,-1):
            if nums[i] % 2 == 0 and len(elements) < count:
                elements.append(nums[i])
    elif type == "odd":
        for i in range(len(nums)-1,-1,-1):
            if nums[i] % 2 != 0 and len(elements) < count:
                elements.append(nums[i])

    elements.reverse()
    return elements

def solve():
    nums = read_number_arr()
    command_input = input()

    while command_input != 'end':
        args = command_input.split(" ")
        command = args[0]

        if command == "exchange":
            index = int(args[1])
            nums = exchange(nums, index)

        elif command == "max":
            type = args[1]
            max_index = max_even_or_odd(nums, type)

            if max_index != -1:
                print(max_index)
            else:
                print("No matches")

        elif command == "min":
            type = args[1]
            min_index = min_even_or_odd(nums, type)

            if min_index != -1:
                print(min_index)
            else:
                print("No matches")

        elif command == "first":
            count = int(args[1])
            type = args[2]
            if count > len(nums) or count < 0:
                print("Invalid count")
                command_input = input()
                continue

            print(first_even_odd(nums, count, type))

        elif command == "last":
            count = int(args[1])
            type = args[2]
            if count > len(nums) or count < 0:
                print("Invalid count")
                command_input = input()
                continue

            print(last_even_odd(nums, count, type))
        command_input = input()
    print(nums)
solve()
