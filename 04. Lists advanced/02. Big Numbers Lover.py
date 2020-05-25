list_str = input().split()
# list_str = sorted(list_str, reverse=True) # returns a list that should be assigned
list_str.sort(reverse=True) # This method returns None

print("".join(list_str))