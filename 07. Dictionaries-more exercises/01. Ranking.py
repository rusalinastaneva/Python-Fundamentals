command_contests = input()
contests = {}
ranking = {}
while command_contests != "end of contests":
    contest = command_contests.split(":")[0]
    password = command_contests.split(":")[1]

    if contest not in contests:
        contests[contest] = password
    command_contests = input()

command_submissions = input()

while command_submissions != "end of submissions":
    contest = command_submissions.split("=>")[0]
    password = command_submissions.split("=>")[1]
    name = command_submissions.split("=>")[2]
    points = int(command_submissions.split("=>")[3])

    if contest in contests and contests[contest] == password:
        if name not in ranking:
            ranking[name] = {contest: points}
        else:
            if contest in ranking[name]:
                if points > ranking[name][contest]:
                    ranking[name][contest] = points
            else:
                ranking[name][contest] = points
    command_submissions = input()

ranking_sum = {k: sum(v_dict.values()) for k, v_dict in ranking.items()} # SUM THE VALUES OF NESTED DICTIONARY
max_points_pair = max(ranking_sum.items(), key=lambda k: k[1]) # GET KEY-VALUE PAIR WITH LARGEST VALUE

print(f'Best candidate is {max_points_pair[0]} with total {max_points_pair[1]} points.')
print("Ranking:")
ranking = dict(sorted(ranking.items()))

for key, inner_map in ranking.items():
    inner_map = dict(sorted(inner_map.items(), key=lambda x: (-x[1])))
    print(key)
    for k, v in inner_map.items():
        print(f'#  {k} -> {v}')
