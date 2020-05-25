# command = input()
# dwarfs = {}
# # {name: {color:physics}
# while command != "Once upon a time":
#     name = command.split(" <:> ")[0]
#     color = command.split(" <:> ")[1]
#     physics = int(command.split(" <:> ")[2])
#
#     if name not in dwarfs:
#         dwarfs[name] = {color: physics}
#     else:
#         if color in dwarfs[name]:
#             if dwarfs[name][color] < physics:
#                 dwarfs[name][color] = physics
#         else:
#             dwarfs[name][color] = physics
#     command = input()
#
# # {name: {color:physics}
# sorted_map = {}
# inner_map = {key: value for dict in dwarfs.values() for key, value in dict.items()}
# print(inner_map)
#
#
# for key, inner_map in dwarfs.items():
#     print(key)
#     inner_map = dict(sorted(inner_map.items()))
#     for k, v in inner_map.items():
#         print(f'{k} {v}')
