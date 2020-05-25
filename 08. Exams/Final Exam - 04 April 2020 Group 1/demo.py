cities = {'Taaar':{"population": 5000, "gold": 6},
          'Tape':{"population": 2500, "gold": 6},
          'Ama':{"population": 50, "gold": 120},
          'Aaak':{"population": 5000, "gold": 120}
          }
cities = dict(sorted(cities.items(), key=lambda y: (-y[1]["gold"], y[0])))
for key, value in cities.items():
    print(f'Key: {key} Population {value["population"]} Gold: {value["gold"]}')
