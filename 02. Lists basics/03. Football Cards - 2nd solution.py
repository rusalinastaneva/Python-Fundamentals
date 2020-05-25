cards = input().split() # A-1 A-5 A-10 B-2
banned_players_team_a = set()
banned_players_team_b = set()

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])

    if team == 'A':
        banned_players_team_a.add(player)
    else:
        banned_players_team_b.add(player)

remaining_team_a = 11 - len(banned_players_team_a)
remaining_team_b = 11 - len(banned_players_team_b)

print(f'Team A - {remaining_team_a}; Team B - {remaining_team_b}')

if remaining_team_b < 7 or remaining_team_a < 7:
    print("Game was terminated")
