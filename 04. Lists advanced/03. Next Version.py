# num = int(input().replace(".", ""))
# new_version = num + 1
#
# print('.'.join(map(str, str(new_version))))

version = int("".join(input().split("."))) + 1
print('.'.join(str(version)))