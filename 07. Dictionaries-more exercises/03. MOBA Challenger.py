command = input()
players = {}
while command != "Season end":
    args = command.split()
    if args[1] == "->":
        player = args[0]
        position = args[2]
        skill = int(args[4])

        if player not in players:
            players[player] = {position: skill}
        else:
            if position in players[player]:
                if players[player][position] < skill:
                    players[player][position] = skill
            else:
                players[player][position] = skill
    else:
        first_player = args[0]
        second_player = args[2]
        if first_player and second_player in players:
            defeated = False
            for key, value in players[first_player].items():
                for k, v in players[second_player].items():
                    if key == k:
                        if value > v:
                            players.pop(second_player)
                            defeated = True
                            break
                        elif value < v:
                            players.pop(first_player)
                            defeated = True
                            break
                if defeated:
                    break
    command = input()

players = dict(sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])))
for key, inner_map in players.items():
    print(f'{key}: {sum(inner_map.values())} skill')
    inner_map = dict(sorted(inner_map.items(), key=lambda k: (-k[1], k[0])))

    for key, value in inner_map.items():
        print(f'- {key} <::> {value}')
