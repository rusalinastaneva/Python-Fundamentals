def is_palindrome(num_str):
        reversed_num = num_str[::-1]
        return True if num_str == reversed_num else False

text = input()
nums = text.split(", ")

for num in nums:
    print(is_palindrome(num))