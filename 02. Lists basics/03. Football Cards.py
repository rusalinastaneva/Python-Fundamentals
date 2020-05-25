cards = input().split() # A-1 A-5 A-10 B-2

team_a = [1] * 11
team_b = [1] * 11

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])

    if team == 'A':
        team_a[player - 1] = 0
    else:
        team_b[player - 1] = 0

print(f'Team A - {sum(team_a)}; Team B - {sum(team_b)}')

if sum(team_b) < 7 or sum(team_a) < 7:
    print("Game was terminated")
